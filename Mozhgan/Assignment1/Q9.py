class Robot:
    def _init_(self, current_position, current_direction, current_time, speed):
        self.current_position = current_position
        self.current_direction = current_direction
        self.current_time = current_time
        self.speed = speed


ROBOT = Robot([0, 0], [1, 0], 0.0, 0.5)
