class Point:
	def reset(self):
		self.x = 0
		self.y = 0

p = Point()
p.reset()
print(p.x, p.y)

"      or       "
p = Point()
Point.reset(p)
print(p.x, p.y)