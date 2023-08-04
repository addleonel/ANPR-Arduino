import time
import pyfirmata
import threading
from massif.utils import StepperLib

# Set the port to match your Arduino board
port = 'COM6'
# Create a new board instance
board = pyfirmata.Arduino(port)
# Start an iterator thread to read analog values from the board
reader = pyfirmata.util.Iterator(board)
reader.start()

# Sound Sensor


def run_sound_sensor():
    # Define the pin connected to the sound sensor
    sound_pin = board.get_pin('a:0:i')  # Analog pin 0, input mode
    led_1 = board.get_pin('d:13:o')

    # Start an iterator thread to read analog values from the board
    it = pyfirmata.util.Iterator(board)
    it.start()

    # Read sound sensor data in a loop
    try:
        while True:
            # Read the sensor value
            sound_value = sound_pin.read()
            if sound_value is not None:
                print("Sound sensor value:", sound_value)
                if sound_value > 0.6:
                    led_1.write(1)
                    time.sleep(3)
                else:
                    led_1.write(0)
            # Delay between readings
            # time.sleep(0.1)

    except KeyboardInterrupt:
        # Clean up and close the connection
        board.exit()


def run_motor():
    # 9, 10, 11, 12 are digital pin numbers and 2038 is the number of steps in the stepper motor I used
    step_ = 2048
    motor = StepperLib.Stepper(step_, board, reader, 9, 10, 11, 12)
    motor.set_speed(100000)

    step_2 = 1024
    while True:
        print(step_2)
        motor.step(step_2)
        time.sleep(1)
        motor.step(-step_2)
        time.sleep(1)


def all_functions():
    run_sound_sensor()
    run_motor()


threading = threading.Thread(target=all_functions)
threading.start()
