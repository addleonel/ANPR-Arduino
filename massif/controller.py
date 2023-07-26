import time
from pyfirmata import Arduino
import pyfirmata

comport='COM5'

board=Arduino(comport)

led_1=board.get_pin('d:12:o')
led_2=board.get_pin('d:11:o')
led_3=board.get_pin('d:10:o')

sound_pin = board.get_pin('a:0:i')  # Analog pin 0, input mode
led_4=board.get_pin('d:13:o')

it = pyfirmata.util.Iterator(board)
it.start()
def turn_on_led(status):
    if status=='BANNED':
        # into db and banned,  red
        led_1.write(1)
        led_2.write(0)
        led_3.write(0)

    if status=='ADMITED':
        # into db and admited, white
        led_1.write(0)
        led_2.write(1)
        led_3.write(0)

    if status=='DETECTED':
        # not in db but is a license plate, yellow
        led_1.write(0)
        led_2.write(0)
        led_3.write(1)

    if status=='NOT DETECTED':
        # not in db and is not a license plate
        led_1.write(0)
        led_2.write(0)
        led_3.write(0)