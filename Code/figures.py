
from graphics import *

class Color(object):
	def __init__(self, r, g, b):
		self.r = r
		self.g = g
		self.b = b

class Hide(object):
	begin = -1
	end = -1
	active = False

class Show(object):
	begin = -1
	end = -1
	active = False

class Move(object):
	begin = -1
	end = -1
	x = -1
	y = -1
	active = False

class Scale(object):
	begin = -1
	end = -1
	size = -1
	active = False

class Vertex(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y


class Figure(object):
	def __init__(self):
		self.hide = Hide()
		self.show = Show()
		self.move = Move()
		self.color = Color(0,0,0)

	def setColor(self, r, g, b):
		self.color.r = r
		self.color.g = g
		self.color.b = b

	def setTypeColor(self, type, color):
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
		return color_rgb(self.color.r, self.color.g, self.color.b)

class L_Circle(Figure):
	def __init__(self, x = 0, y = 0, radius = 0):
		super(self.__class__, self).__init__()
		self.radius = radius
		self.center = Vertex(x, y)
		self.totalNumVertices = 1
		self.numVertices = 0

	def setNextVertex(self, x, y):
		# if self.numVertices >= self.totalNumVertices:
		# 	return False
		self.center.x = x
		self.center.y = y
		# self.numVertices += 1
		return True

	def setSize(self, size):
		self.radius = size

	def getSize(self):
		return self.radius

	def getPointCenter(self):
		return Point(self.center.x, self.center.y)

	def reset(self):
		self.numVertices = 0

class L_Triangle(Figure):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.vertices = [Vertex(0,0), Vertex(0,0), Vertex(0,0)]
		self.totalNumVertices = 3
		self.numVertices = 0
	
	def setVertex(self, num, x, y):
		self.vertices[num].x = x
		self.vertices[num].y = y

	def setNextVertex(self, x, y):
		if self.numVertices >= self.totalNumVertices:
			return False
		self.vertices[self.numVertices].x = x
		self.vertices[self.numVertices].y = y
		self.numVertices += 1
		return True

	def getVertex(self, num):
		return (self.vertices[num].x, self.vertices[num].y)

	def getPointsList(self):
		l = []
		for vertex in self.vertices:
			l.append( Point(vertex.x, vertex.y) )
		return l

	def reset(self):
		self.numVertices = 0

class L_Rectangle(Figure):
	def __init__(self, x1 = 0, y1 = 0, x2 = 0, y2 = 0):
		super(self.__class__, self).__init__()
		self.vertices = [Vertex(0,0), Vertex(0,0)]
		self.totalNumVertices = 2
		self.numVertices = 0

	def setNextVertex(self, x, y):
		if self.numVertices >= self.totalNumVertices:
			return False
		self.vertices[self.numVertices].x = x
		self.vertices[self.numVertices].y = y
		self.numVertices += 1
		return True

	def getPoints(self):
		return (Point(self.vertices[0].x, self.vertices[0].y), Point(self.vertices[1].x, self.vertices[1].y))

	def reset(self):
		self.numVertices = 0

# class L_Point(Figure):
# 	def __init__(self, x = 0, y = 0):
# 		super(self.__class__, self).__init__()
# 		self.center = Vertex(x, y)

# 	def getPoint(self):
# 		return Point(self.center.x, self.center.y)

class L_Square(Figure):
	def __init__(self, x = 0, y = 0, size = 0):
		super(self.__class__, self).__init__()
		self.size = size
		self.v1 = Vertex(x, y)
		self.v2 = Vertex(x+size, y+size)
		self.totalNumVertices = 1
		self.numVertices = 0

	def setNextVertex(self, x, y):
		if self.numVertices >= self.totalNumVertices:
			return False
		self.v1.x = x
		self.v1.y = y
		self.numVertices += 1
		return True

	def setSize(self, size):
		self.v2.x = self.v1.x + size
		self.v2.y = self.v1.y + size

	def getPoints(self):
		return (Point(self.v1.x, self.v1.y), Point(self.v2.x, self.v2.y))

	def reset(self):
		self.numVertices = 0


class L_Polygon(Figure):
	def __init__(self, numVertices = 0):
		super(self.__class__, self).__init__()
		self.vertices = []
		self.numVertices = numVertices
		self.numVertices = 0

	def setVertex(self, num, x, y):
		self.vertices[num].x = x
		self.vertices[num].y = y

	def setNextVertex(self, x, y):
		self.vertices.append(Vertex(x, y))
		self.numVertices += 1
		return True

	def getVertex(self, num):
		return (self.vertices[num].x, self.vertices[num].y)

	def getPointsList(self):
		l = []
		for vertex in self.vertices:
			l.append( Point(vertex.x, vertex.y) )
		return l

	def addVertex(self, x, y):
		self.vertices.append(Vertex(x,y))

	def reset(self):
		self.numVertices = 0

#NOT READY
class L_Line(Figure):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.vertices = [Vertex(0,0), Vertex(0,0)]
		self.totalNumVertices = 2
		self.numVertices = 0

	def setNextVertex(self, x, y):
		if self.numVertices >= self.totalNumVertices:
			return False
		self.vertices[self.numVertices].x = x
		self.vertices[self.numVertices].y = y
		self.numVertices += 1
		return True

	def getPoints(self):
		return (Point(self.vertices[0].x, self.vertices[0].y), Point(self.vertices[1].x, self.vertices[1].y))

	def reset(self):
		self.numVertices = 0


##NO STAR #@$% that!