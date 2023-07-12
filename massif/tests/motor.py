from time import sleep
import pyfirmata
from massif.utils import StepperLib

# Set the port to match your Arduino board
port = 'COM6'

# Create a new board instance
board = pyfirmata.Arduino(port)

reader = pyfirmata.util.Iterator(board) # reads inputs of the circuit
reader.start()

# 9, 10, 11, 12 are digital pin numbers and 2038 is the number of steps in the stepper motor I used
step_ = 2048
motor = StepperLib.Stepper(step_, board, reader, 9, 10, 11, 12)
motor.set_speed(100000)

step_2 = 1024
while True:
  print(step_2)
  motor.step(step_2)
  sleep(1)
  motor.step(-step_2)
  sleep(1)
        