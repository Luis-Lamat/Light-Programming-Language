
from graphics import *
import math

class Color(object):
	"""Color class """
	def __init__(self, r, g, b):
		self.r = r
		self.g = g
		self.b = b

class Vertex(object):
	"""Vertex class """
	def __init__(self, x, y):
		self.x = x
		self.y = y


class Figure(object):
	"""Figure class """
	def __init__(self):
		self.color = Color(0,0,0)
		self.avgx = 0.0
		self.avgy = 0.0
		self.numVertices = 0

	def setColor(self, r, g, b):
		"""Set color
		
		Sets color from parameters and stores on Color class
		
		Arguments:
			r {int} -- 0...255
			g {int} -- 0...255
			b {int} -- 0...255
		"""
		self.color.r = r
		self.color.g = g
		self.color.b = b

	def setTypeColor(self, type, color):
		"""Set type color
		
		Sets the specific color of type r, g or b
		
		Arguments:
			type {char} -- 'r', 'g' or 'b'
			color {int} -- 0...255
		
		Returns:
			bool -- [description]
		"""
		if color >= 0:
			if type == "r" :
				self.color.r = color % 256
			elif type == "g":
				self.color.g = color % 256
			elif type == "b":
				self.color.b = color % 256
			else :
				pass
			return True
		else:
			return False

	def getColor(self):
		"""gets color
		
		Gets the color and builds a color from graphics library
		
		Returns:
			color_rgb -- object from color_rgb
		"""
		return color_rgb(self.color.r, self.color.g, self.color.b)

	def move(self, x, y):
		"""move
		
		Moves the object
		
		Arguments:
			x {int} -- int
			y {int} -- int
		"""
		for ver in self.vertices:
			ver.x += x
			ver.y += y

	def reset(self):
		"""reset number of vertices
		
		Reset number of vertices
		"""
		self.numVertices = 0


class L_Circle(Figure):
	""" Cirlce class """
	def __init__(self, x = 0, y = 0, radius = 0):
		super(self.__class__, self).__init__()
		self.radius = radius
		self.center = Vertex(x, y)
		self.totalNumVertices = 1

	def setNextVertex(self, x, y):
		"""Set next vertex
		
		Sets circle vertex
		
		Arguments:
			x {int} -- int
			y {int} -- int
		
		Returns:
			bool -- True
		"""
		self.center.x = x
		self.center.y = y
		return True

	def move(self, x, y):
		"""Move
		
		Moves circle
		
		Arguments:
			x {int} -- int
			y {int} -- int
		"""
		self.center.x += x
		self.center.y += y

	def setSize(self, size):
		"""Set size
		
		Set circle size
		
		Arguments:
			size {int} -- int
		"""
		self.radius = size

	def getSize(self):
		"""Get size
		
		Get circle size
		
		Returns:
			int -- int
		"""
		return self.radius

	def getPointCenter(self):
		"""Get circle point
		
		Get the center point of circle, and returns a Point object
		
		Returns:
			Point -- point object
		"""
		return Point(self.center.x, self.center.y)

class L_Triangle(Figure):
	""" Triangel Class """
	def __init__(self):
		super(self.__class__, self).__init__()
		self.vertices = [Vertex(0,0), Vertex(0,0), Vertex(0,0)]
		self.totalNumVertices = 3
	
	def setVertex(self, num, x, y):
		"""Set vertex
		
		Set a vertex on index num
		
		Arguments:
			num {int} -- int
			x {int} -- int
			y {int} -- int
		"""
		self.vertices[num].x = x
		self.vertices[num].y = y

	def setNextVertex(self, x, y):
		"""Set next vertex
		
		Set free vertex, returns True if possible False otherwise
		
		Arguments:
			x {int} -- int
			y {int} -- int
		
		Returns:
			bool -- Bool
		"""
		if self.numVertices >= self.totalNumVertices:
			return False
		self.vertices[self.numVertices].x = x
		self.vertices[self.numVertices].y = y
		self.numVertices += 1
		return True

	def getVertex(self, num):
		"""Get Vertex
		
		Returns tupple with x and y values
		
		Arguments:
			num {int} -- int
		"""
		return (self.vertices[num].x, self.vertices[num].y)

	def getPointsList(self):
		"""Get points list
		
		Gets the points from vertex list
		
		Returns:
			List -- vertex list
		"""
		l = []
		for vertex in self.vertices:
			l.append( Point(vertex.x, vertex.y) )
		return l

class L_Rectangle(Figure):
	def __init__(self, x1 = 0, y1 = 0, x2 = 0, y2 = 0):
		super(self.__class__, self).__init__()
		self.vertices = [Vertex(0,0), Vertex(0,0)]
		self.totalNumVertices = 2

	def setNextVertex(self, x, y):
		"""Set next vertex
		
		Set free vertex, returns True if possible False otherwise
		
		Arguments:
			x {int} -- int
			y {int} -- int
		
		Returns:
			bool -- Bool
		"""
		if self.numVertices >= self.totalNumVertices:
			return False
		self.vertices[self.numVertices].x = x
		self.vertices[self.numVertices].y = y
		self.numVertices += 1
		return True

	def getPoints(self):
		"""Get points list
		
		Gets the points from vertex list
		
		Returns:
			List -- vertex list
		"""
		return (Point(self.vertices[0].x, self.vertices[0].y), Point(self.vertices[1].x, self.vertices[1].y))


class L_Square(Figure):
	""" Square class """

	def __init__(self, x = 0, y = 0, size = 0):
		super(self.__class__, self).__init__()
		self.size = size
		self.v1 = Vertex(x, y)
		self.v2 = Vertex(x+size, y+size)
		self.totalNumVertices = 1

	def setNextVertex(self, x, y):
		"""Set next vertex
		
		Set free vertex, returns True if possible False otherwise
		
		Arguments:
			x {int} -- int
			y {int} -- int
		
		Returns:
			bool -- Bool
		"""
		if self.numVertices >= self.totalNumVertices:
			return False
		self.v1.x = x
		self.v1.y = y
		self.numVertices += 1
		return True

	def setSize(self, size):
		"""Set size
		
		Set square size
		
		Arguments:
			size {int} -- int
		"""
		self.v2.x = self.v1.x + size
		self.v2.y = self.v1.y + size

	def getPoints(self):
		"""Get points list
		
		Gets the points from vertex list
		
		Returns:
			List -- vertex list
		"""
		return (Point(self.v1.x, self.v1.y), Point(self.v2.x, self.v2.y))

	def move(self, x, y):
		"""Move
		
		Moves square in x and y
		
		Arguments:
			x {int} -- int
			y {int} -- int
		"""
		self.v1.x += x
		self.v1.y += y
		self.v2.x += x
		self.v2.y += y

class L_Polygon(Figure):
	""" Polygon class """
	def __init__(self, numVertices = 0):
		super(self.__class__, self).__init__()
		self.vertices = []
		self.numVertices = numVertices

	def setVertex(self, num, x, y):
		"""Set vertex
		
		Set a vertex on index num
		
		Arguments:
			num {int} -- int
			x {int} -- int
			y {int} -- int
		"""
		self.vertices[num].x = x
		self.vertices[num].y = y

	def setNextVertex(self, x, y):
		"""Set next vertex
		
		Set free vertex, returns True if possible False otherwise
		
		Arguments:
			x {int} -- int
			y {int} -- int
		
		Returns:
			bool -- Bool
		"""
		self.vertices.append(Vertex(x, y))
		self.numVertices += 1
		return True

	def getVertex(self, num):
		"""Get Vertex
		
		Returns tupple with x and y values
		
		Arguments:
			num {int} -- int
		"""
		return (self.vertices[num].x, self.vertices[num].y)

	def getPointsList(self):
		"""Get points list
		
		Gets the points from vertex list
		
		Returns:
			List -- vertex list
		"""
		l = []
		for vertex in self.vertices:
			l.append( Point(vertex.x, vertex.y) )
		return l

	def addVertex(self, x, y):
		"""Get points list
		
		Gets the points from vertex list
		
		Returns:
			List -- vertex list
		"""
		self.vertices.append(Vertex(x,y))


#NOT READY
class L_Line(Figure):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.vertices = [Vertex(0,0), Vertex(0,0)]
		self.totalNumVertices = 2

	def setNextVertex(self, x, y):
		"""Set next vertex
		
		Set free vertex, returns True if possible False otherwise
		
		Arguments:
			x {int} -- int
			y {int} -- int
		
		Returns:
			bool -- Bool
		"""
		if self.numVertices >= self.totalNumVertices:
			return False
		self.vertices[self.numVertices].x = x
		self.vertices[self.numVertices].y = y
		self.numVertices += 1
		return True

	def getPoints(self):
		"""Get Vertex
		
		Returns tupple with x and y values
		
		Arguments:
			num {int} -- int
		"""
		return (Point(self.vertices[0].x, self.vertices[0].y), Point(self.vertices[1].x, self.vertices[1].y))

