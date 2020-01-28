class Rectangle(object):
	def __init__(self, width, height):
		self._width = width
		self._height = height
		
r = Rectangle(5, 6)
# direct access of protected member
print("Width: {:d}".format(r._width))