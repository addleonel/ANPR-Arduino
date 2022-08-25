from string import hexdigits
import cv2
import numpy as np
import pytesseract
from PIL import Image


cap = cv2.VideoCapture(0)
width = 1280
height = 720

cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

cText = ''
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
while True:
    ret, frame = cap.read()

    if ret == False:
        break
    # print(cText)
    cv2.rectangle(frame, (870, 750), (1070, 850), (0, 0, 0), cv2.FILLED)
    # cv2.putText(frame, cText[0:7], (900, 810), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 5)
    cv2.putText(frame, cText[0:7], (45, 90), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 5)
    
    al, an, c = frame.shape

    x1 = int(an/3)
    x2 = int(x1*2)

    y1 = int(al/3)
    y2 = int(y1 * 2)

    cv2.rectangle(frame, (x1 + 160, y1 + 500), (1120, 960), (0, 0, 0), cv2.FILLED)
    cv2.putText(frame, 'Procesing', (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    # cv2.putText(frame, 'Procesing', (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
    
    cut = frame[y1:y2, x1:x2]
    
    mB = np.matrix(cut[:, :, 0])
    mG = np.matrix(cut[:, :, 1])
    mR = np.matrix(cut[:, :, 2])

    color = cv2.absdiff(mG, mB)
    # color = cv2.absdiff(mB, mR)
    
    print(color)
    _, umbral = cv2.threshold(color, 40, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(umbral, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)
    
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 500 and area < 5000:
            x, y, w, h = cv2.boundingRect(contour)

            xpi = x + x1
            ypi = y + y1

            xpf = x + w + x1
            ypf = y + h + y1

            cv2.rectangle(frame, (xpi, ypi), (xpf, ypf), (236, 29, 50), 2)

            placa = frame[ypi:ypf, xpi:xpf]

            hp, wp, cp = placa.shape

            Mva = np.zeros((hp, wp))

            mBp = np.matrix(placa[:, :, 0])
            mGp = np.matrix(placa[:, :, 1])
            mRp = np.matrix(placa[:, :, 2])

            for col in range(0, hp):
                for fil in range(0, wp):
                    Max = max(mRp[col, fil], mGp[col, fil], mBp[col, fil])
                    Mva[col,fil] = 255 - Max

            _, bin = cv2.threshold(Mva, 150, 255, cv2.THRESH_BINARY)

            bin = bin.reshape(hp, wp)
            bin = Image.fromarray(bin)
            bin = bin.convert("L")

            if hp >= 36 and wp >= 82:
                config = '--psm 1'
                text = pytesseract.image_to_string(bin, config=config)

                if len(text) >= 5:
                    
                    cText = text
            
            break
    cv2.imshow('vehicle', frame)

    k = cv2.waitKey(1)

    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()