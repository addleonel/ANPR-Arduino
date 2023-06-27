import pyfirmata

comport='COM3'

board=pyfirmata.Arduino(comport)

led_1=board.get_pin('d:13:o')
led_2=board.get_pin('d:12:o')
# led_3=board.get_pin('d:8:o')
# led_4=board.get_pin('d:7:o')
# led_5=board.get_pin('d:4:o')

def turn_on_led(found_plate):
    if found_plate==True:
        led_1.write(1)
        led_2.write(0)

    if found_plate==False:
        led_1.write(0)
        led_2.write(1)