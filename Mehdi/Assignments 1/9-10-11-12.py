import time

class Robot:
    def __init__(self, p=[0, 0], d=[1, 0], s=4, t=0.0):
        self.position = p
        self.direction = d
        self.time = t
        self.speed = s
        self.start_time = time.time()

    def __repr__(self):
        robot1.time = time.time() - self.start_time
        rep = '\nPosition: ' + str(self.position) + '\nDirection: ' + str(self.direction) \
            + '\nSpeed: ' + str(self.speed) + '\nTime: ' + str(self.time) + '\n'
        return rep

    def wait(self, t):
        temp = self.speed
        self.speed = 0
        time.sleep(t)
        self.speed = temp
        
    def move_forward(self, t):
        time.sleep(t)
        self.position = [self.position[0] + (self.direction[0]*self.speed*t), \
            self.position[1] + (self.direction[1]*self.speed*t)]

    def rotate_right(self):
        self.direction = [self.direction[1], self.direction[0] * -1]

    def rotate_left(self):
        self.direction = [self.direction[1] * -1, self.direction[0]]

robot1 = Robot()
def move_square(side_length):

    robot1.time = time.time() - robot1.start_time
    print(repr(robot1))
    forward_time = side_length / robot1.speed
    print ('\nrobot moving ...\n')
    robot1.move_forward(forward_time)
    print(repr(robot1))
    print ('\nrobot turning ...\n')
    robot1.rotate_left()
    print(repr(robot1))
    print ('\nrobot moving ...\n')
    robot1.move_forward(forward_time)
    print(repr(robot1))
    print ('\nrobot turning ...\n')
    robot1.rotate_left()
    print(repr(robot1))
    print ('\nrobot moving ...\n')
    robot1.move_forward(forward_time)
    print(repr(robot1))
    print ('\nrobot turning ...\n')
    robot1.rotate_left()
    print(repr(robot1))
    print ('\nrobot moving ...\n')
    robot1.move_forward(forward_time)
    print(repr(robot1))


move_square(10)
