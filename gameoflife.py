class Game(object):
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.current_world = self.create_world(width, height)
		self.next_world = self.create_world(width, height)

	@staticmethod
	def create_world(width, height):
		return [
			[False] * height for i in range(width)
		]

	def get(self, x, y):
		xx = min(self.width - 1, max(0, x))
		yy = min(self.height - 1, max(0, y))
		return self.current_world[xx][yy]

	def set(self, x, y, value):
		self.current_world[x][y] = value

	def check_next_state(self, x, y):
		count = 0
		for i in range(-1, 2):
			for j in range(-1, 2):
				if self.get(x+i, y+j) is True:
					count += 1
		if self.get(x, y) is True:
			return count in [3, 4]
		else:
			return count == 3