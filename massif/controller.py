import time
from pyfirmata import Arduino

comport='COM5'

board=Arduino(comport)

led_1=board.get_pin('d:13:o')
led_2=board.get_pin('d:12:o')
led_3=board.get_pin('d:8:o')
# pin_7=board.get_pin('d:7:o')
# led_5=board.get_pin('d:4:o')

def turn_on_led(status):
    if status=='BANNED':
        # into db and banned
        led_1.write(1)
        led_2.write(0)
        led_3.write(0)

    if status=='ADMITED':
        # into db and admited
        led_1.write(0)
        led_2.write(1)
        led_3.write(0)

    if status=='DETECTED':
        # not in db but is a license plate
        led_1.write(0)
        led_2.write(0)
        led_3.write(1)

    if status=='NOT DETECTED':
        # not in db and is not a license plate
        led_1.write(0)
        led_2.write(0)
        led_3.write(0)