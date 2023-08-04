import os
import time
import sqlite3
import cv2
import pytesseract
import numpy as np
from PIL import Image
from datetime import datetime
from consume import is_banned, make_match, post_captured_plates
from controller import turn_on_led, sound_pin, led_4
from camera import cameras


def run_engine():
    # Directory to save the captured photos
    output_dir = "../output_photo/plate"
    output_dir_car = "../output_photo/car"

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    if not os.path.exists(output_dir_car):
        os.makedirs(output_dir_car)

    # Connect to the SQLite database
    conn = sqlite3.connect('../license_plates.db')
    connexec = conn.cursor()

    # Create the table if it doesn't exist
    connexec.execute('''CREATE TABLE IF NOT EXISTS plates
                (id INTEGER PRIMARY KEY AUTOINCREMENT, plate_number TEXT)''')

    cap = cv2.VideoCapture(cameras[0]["ip"])
    width = 1380
    height = 750

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    cText = ''
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    while True:

        sound_value = sound_pin.read()
        if sound_value is not None:
            print("Sound sensor value:", sound_value)
            if sound_value > 0.64:
                led_4.write(1)
                time.sleep(3)
            else:
                led_4.write(0)
        ret, frame = cap.read()

        if ret == False:
            break
        cv2.rectangle(frame, (870, 750), (1070, 850),
                      (58, 252, 61), cv2.FILLED)
        cv2.putText(frame, "HELLO", (900, 810),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 5)

        al, an, c = frame.shape

        x1 = int(an/6)
        x2 = int(x1 * 5)

        y1 = int(al/6)
        y2 = int(y1 * 5)

        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 255, 255), 2)

        cut = frame[y1:y2, x1:x2]

        mB = np.matrix(cut[:, :, 0])
        mG = np.matrix(cut[:, :, 1])
        mR = np.matrix(cut[:, :, 2])

        color = cv2.absdiff(mG, mB)  # yellow

        _, umbral = cv2.threshold(color, 40, 255, cv2.THRESH_BINARY)

        contours, _ = cv2.findContours(
            umbral, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(
            contours, key=lambda x: cv2.contourArea(x), reverse=True)

        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 100 and area < 6000:
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
                        Mva[col, fil] = 255 - Max

                _, bin = cv2.threshold(Mva, 150, 255, cv2.THRESH_BINARY)

                bin = bin.reshape(hp, wp)
                bin = Image.fromarray(bin)
                bin = bin.convert("L")

                # if hp >= 100 and wp >= 200:
                # if hp >= 40 and wp >= 90:
                config = '--psm 1'
                text = pytesseract.image_to_string(bin, config=config)
                # count_texts = []
                turn_on_led('NOT DETECTED')
                if len(text) >= 7:
                    # Save the frame as an image
                    cText = text
                    turn_on_led('DETECTED')
                    print("License plate detected:", cText)

                    # license
                    filename = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
                    output_path = os.path.join(output_dir, f"{filename}.jpg")
                    cv2.imwrite(output_path, placa)

                    # car
                    filename_car = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
                    output_path_car = os.path.join(
                        output_dir_car, f"{filename_car}.jpg")
                    cv2.imwrite(output_path_car, frame)

                    files = {
                        'image_license': open(output_path, 'rb'),
                        'image_car': open(output_path_car, 'rb')
                    }

                    data = {
                        'plate': cText,
                    }

                    post_captured_plates(files, data)

                    # os.remove(output_path)
                    # os.remove(output_path_car)

                    if make_match(cText.strip()):  # make match with the database
                        cv2.putText(frame, "ENCONTRADO", (45, 90),
                                    cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 5)
                        if is_banned(cText.strip()):  # check if the license plate is banned
                            turn_on_led('BANNED')
                            print("Placa Baneada")
                            cv2.putText(frame, "BANEADO", (45, 150),
                                        cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 5)
                        else:
                            turn_on_led('ADMITED')
                            print("Placa Admitida")
                            cv2.putText(frame, "ADMITIDO", (45, 150),
                                        cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 5)

                    connexec.execute(
                        "INSERT INTO plates (plate_number) VALUES (?)", (cText,))
                    conn.commit()

                break
        cv2.imshow('FALCONI', frame)

        k = cv2.waitKey(1)

        if k == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run_engine()
