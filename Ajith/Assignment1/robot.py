import time
import math

class robot:

	def __init__(self, currentPosition=[0,0], currentDirection=[1,0], currentTime=0, currentSpeed=0.5):
		self.currentPosition = currentPosition
		self.currentDirection = currentDirection
		self.currentTime = currentTime
		self.currentSpeed = currentSpeed

	def __repr__(self):
		return f'Current Position: {self.currentPosition}\nCurrent Direction: {self.currentDirection}\nCurrent Time: {self.currentTime}'

	def wait(self, Time):
		speed = self.currentSpeed
		self.currentSpeed = 0
		time.sleep(Time)
		self.currentSpeed = speed
		self.currentTime += Time

	def move_forward(self, Time):
		timer = 0
		timeStep = 0.001
		processingTime = 0
		while timer <= Time:
			startTime = time.time()
			self.currentPosition =  [sum(i) for i in zip(self.currentPosition,[i * self.currentSpeed * (timeStep) for i in self.currentDirection])]
			self.currentTime += timeStep
			timer += timeStep
			endTime = time.time()
			processingTime = endTime - startTime
			time.sleep(timeStep - processingTime)

	def rotate_right(self):
		self.currentDirection = [self.currentDirection[1], -self.currentDirection[0]]

	def rotate_left(self):
		self.currentDirection = [-self.currentDirection[1], self.currentDirection[0]]

	def move_square(self, side):
		sideTraverse = side/self.currentSpeed
		for _ in range(0,4):
			self.move_forward(sideTraverse)
			self.wait(2)
			self.rotate_right


r2d2 = robot()
print(r2d2)
r2d2.wait(10)
r2d2.move_forward(10)
r2d2.rotate_right()
r2d2.rotate_left()
r2d2.move_square(1)