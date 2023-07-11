from pyfirmata import Arduino, util, STRING_DATA
import time
board = Arduino('COM5')

def msg( text ):
    if text:
        board.send_sysex( STRING_DATA, util.str_to_two_byte_iter( text ) )
    else:
        board.send_sysex( STRING_DATA, util.str_to_two_byte_iter( ' ' ) )

start_time = time.time()

while (True): 
    elapsed_time = time.time() - start_time
    if elapsed_time > 5:
        msg('Hola')
        start_time = time.time()
    else:
        msg(' ')
    time.sleep(1)