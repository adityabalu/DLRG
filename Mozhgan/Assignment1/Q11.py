import time


class Robot:
    def _init_(self, current_position, current_direction, current_time, speed):
        self.current_position = current_position
        self.current_direction = current_direction
        self.current_time = current_time
        self.speed = speed

    def _repr_(self):
        return f'Robot\'s current position, direction, and time are: ("{self.current_position}","{self.current_direction}",{self.current_time}), respectively.'

    def wait(self, time1):

        self.speed = 0.0
        time.sleep(time1)

    def move_forward(self, time):
        self.speed = 0.5

    def rotate_right(self):

        if self.current_direction == [1, 0]:
            self.current_direction = [0, -1]

        elif self.current_direction == [0, -1]:
            self.current_direction = [-1, 0]

        elif self.current_direction == [-1, 0]:
            self.current_direction = [0, 1]

        elif self.current_direction == [0, 1]:
            self.current_direction = [1, 0]

    def rotate_left(self):

        if self.current_direction == [1, 0]:
            self.current_direction = [0, 1]

        elif self.current_direction == [0, 1]:
            self.current_direction = [-1, 0]

        elif self.current_direction == [-1, 0]:
            self.current_direction = [0, -1]

        elif self.current_direction == [0, -1]:
            self.current_direction = [1, 0]


ROBOT = Robot([0, 0], [1, 0], 0.0, 0.5)

print(repr(ROBOT))
