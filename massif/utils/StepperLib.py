
from time import sleep


class Stepper():
    # for a 4 control wire stepper
    # total steps is the total number of steps per revolution, which is 2038
    def __init__(self, total_steps, board, reader, pin_1, pin_2, pin_3, pin_4):

        # sets up the thing so it will mesh with the arduino
        # initializes the pins as outputs
        self.pin_1 = board.get_pin('d:%s:o' % (pin_1))
        self.pin_2 = board.get_pin('d:%s:o' % (pin_2))
        self.pin_3 = board.get_pin('d:%s:o' % (pin_3))
        self.pin_4 = board.get_pin('d:%s:o' % (pin_4))
        # led for testing

        # led = board.get_pin('d:12:o')
        # led.write(1)

        self.step_number = 0  # what number of steps are going to be turned
        self.direction = 0
        self.total_steps = total_steps  # total number of steps per revolution
        self.step_delay = 0  # time delay between steps

    def set_speed(self, what_speed):
        # sets the speed. number is arbitrary but the smaller the delay the faster it runs
        self.step_delay = (self.total_steps / (1000000 * what_speed))
        # print(self.step_delay)

    def step(self, steps_to_move):
        # sets forward and backward
        if steps_to_move > 0:
            self.direction = 1
        if steps_to_move < 0:
            self.direction = 0

        # sets the number of steps that still need to be turned
        steps_left = abs(steps_to_move)

        # while this still needs to be turned, it starts with a delay and then depending on
        # the direction, steps in one direction and then also has a reset for when the
        # step number hits the max or min limits
        while steps_left > 0:
            sleep(self.step_delay)
            if self.direction == 1:
                self.step_number += 1
                if self.step_number == self.total_steps:
                    self.step_number = 0
            else:
                if self.direction == 0:
                    self.step_number -= 1
                    if self.step_number == 0:
                        self.step_number = self.total_steps

                    # print(str(self.step_number))

            steps_left -= 1
            # calls method to actually turn it
            self.step_motor(self.step_number % 8)

    def step_motor(self, this_step):
        # the binary numbers turn it. not sure why, pulled numbers from the github
        # use half steps so that it can turn backwards
        if this_step == 0:
            self.pin_1.write(1)
            self.pin_2.write(0)
            self.pin_3.write(0)
            self.pin_4.write(0)
        elif this_step == 1:
            self.pin_1.write(1)
            self.pin_2.write(1)
            self.pin_3.write(0)
            self.pin_4.write(0)
        elif this_step == 2:
            self.pin_1.write(0)
            self.pin_2.write(1)
            self.pin_3.write(0)
            self.pin_4.write(0)
        elif this_step == 3:
            self.pin_1.write(0)
            self.pin_2.write(1)
            self.pin_3.write(1)
            self.pin_4.write(0)
        elif this_step == 4:
            self.pin_1.write(0)
            self.pin_2.write(0)
            self.pin_3.write(1)
            self.pin_4.write(0)
        elif this_step == 5:
            self.pin_1.write(0)
            self.pin_2.write(0)
            self.pin_3.write(1)
            self.pin_4.write(1)
        elif this_step == 6:
            self.pin_1.write(0)
            self.pin_2.write(0)
            self.pin_3.write(0)
            self.pin_4.write(1)
        elif this_step == 7:
            self.pin_1.write(1)
            self.pin_2.write(0)
            self.pin_3.write(0)
            self.pin_4.write(1)
