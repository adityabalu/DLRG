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
        self.current_time += time1

    def move_forward(self, time2):
        self.speed = 0.5
        x = time2 * self.speed
        result = [item * x for item in self.current_direction]
        new_position = list()
        for item1, item2 in zip(self.current_position, result):
            item = item1 + item2
            new_position.append(item)
        self.current_position = new_position
        self.current_time += time2

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


# print(repr(ROBOT))

def move_square(side_length):
    ROBOT = Robot([0, 0], [1, 0], 0.0, 0.5)
    ROBOT.move_forward(side_length / 0.5)
    print(ROBOT.current_position)
    ROBOT.rotate_left()
    ROBOT.move_forward(side_length / 0.5)
    print(ROBOT.current_position)
    ROBOT.rotate_left()
    ROBOT.move_forward(side_length / 0.5)
    print(ROBOT.current_position)
    ROBOT.rotate_left()
    ROBOT.move_forward(side_length / 0.5)
    print(ROBOT.current_position)


move_square(10.0)
