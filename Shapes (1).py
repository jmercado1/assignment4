import math


class Shape:
	def __init__(self):
		raise NotImplementedError()

	def GetArea(self): pass
	def GetPerimeter(self): pass


class Polygon(Shape):
	def __init__(self, sideLength:float, sides:int):
		''' A representation of a regular polygon defined by sides and side length.

		Math functions will be pulled from the wiki page:
		https://en.wikipedia.org/wiki/Regular_polygon

		Arguments:
			sideLength(float): The length of the sides. Regular polygons have congruent side lengths. Must be a positive, non-zero number.
			sides(int): The number of sides that the regular polygon will have. Must be a number larger than 2.
		'''
		# Validating side length
		if sideLength <= 0:
			raise ValueError(f'sideLength must by a positive, non-zero number. Received `{sideLength}`.')

		# Validating side count
		if sides < 3:
			raise ValueError(f'side count must be a number larger than 2. Received `{sides}`')

		# Setting member variables now that we've validated input
		self._sideLength = sideLength
		self._sides = sides

	def GetArea(self) -> float:
		''' Gets the area of the regular polygon.

		Returns: A float representing the area of the regular polygon.
		'''
		cotComponent = (
			math.cos(math.pi / self._sides)
			/
			math.sin(math.pi / self._sides)
		)

		return (self._sides / 4) * (self._sideLength ** 2) * cotComponent

	def GetPerimeter(self) -> float:
		''' Gets the perimeter of the regular polygon.

		Returns: A float representing the perimeter of the regular polygon.
		'''
		return self._sideLength * self._sides


class Circle(Shape):
	def __init__(self, radius):
		''' A representation of a perfect circle.

		Math functions will be pulled from the wiki page:
		https://en.wikipedia.org/wiki/Circle

		Arguments:
			radius(float): The distance between the center point and the outside of the circle.
		'''
		# Validating radius
		if radius <= 0:
			raise ValueError(f'radius must by a positive, non-zero number. Received `{radius}`.')

		# Eager loading the area and perimeter
		self._area = math.pi * (radius ** 2)
		self._peri = 2 * math.pi * radius

	def GetArea(self) -> float:
		''' Gets the area of the perfect circle.

		Return: A float representing the area of the perfect circle.
		'''
		return self._area

	def GetPerimeter(self) -> float:
		''' Gets the perimeter of the perfect circle.

		Return: A float representing the perimeter of the perfect circle.
		'''
		return self._peri