import math

class Robot():
	def __init__(self, origin=[0, 0], speed=0.5, current_dir=[1,0], current_time=0):
		self.origin = origin
		self.speed = speed
		self.current_dir = current_dir
		self.current_pos = origin
		self.current_time = current_time

	def __repr__(self):

		return '{}\'s Current position is {!r}, current direction is {!r} and current time is {!r}'.format(self.__class__.__name__, self.current_pos, self.current_dir, self.current_time)

	def wait(self, time):
		self.current_time += time

	def move_forward(self, time):
		self.current_pos[0] += self.speed * self.current_dir[0] * time
		self.current_pos[1] += self.speed * self.current_dir[1] * time
		self.current_time += time

	def rotate_right(self):
		x = self.current_dir[0] * 0.0  - self.current_dir[1] * -1.0 # Using Rotation Matrix
		y = self.current_dir[0] * -1.0 + self.current_dir[1] * 0.0 
		self.current_dir = [x, y]

	def rotate_left(self):
		theta = math.pi/2
		x = self.current_dir[0] * 0.0 - self.current_dir[1] * 1.0
		y = self.current_dir[0] * 1.0 + self.current_dir[1] * 0.0
		self.current_dir = [x, y]


def move_square(side_length):
	robot = Robot()
	time = side_length/robot.speed
	print(robot)
	
	robot.move_forward(time) # [side_length, 0]
	print(robot)
	robot.wait(5)
	print(robot)
	robot.rotate_left()
	print(robot)
	robot.move_forward(time) # [side_length, side_length]
	print(robot)
	robot.wait(5)
	print(robot)
	robot.rotate_left()
	print(robot)
	robot.move_forward(time) # [0, side_length]
	print(robot)
	robot.wait(5)
	print(robot)
	robot.rotate_left()
	print(robot)
	robot.move_forward(time) # [0, 0]
	print(robot)
	robot.wait(5)
	print(robot)
		

if __name__ == '__main__':
	move_square(side_length=10)