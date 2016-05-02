from graphics import *
from figures import *
import time

cir = L_Circle(50, 50, 10)
cir.setColor(255,0,0)

triangle = L_Triangle()
triangle.setColor(0,255,0)
triangle.setVertex(0, 10, 10)
triangle.setVertex(1, 50, 30)
triangle.setVertex(2, 20, 40)

ply = L_Polygon(5)
ply.addVertex(10.5, 10.5)
ply.addVertex(30.5, 30.5)
ply.addVertex(40.5, 10.5)
ply.addVertex(50.5, 10.5)
ply.addVertex(60.5, 20.5)
ply.setColor(255,200,0)

rect = L_Rectangle(200, 200, 250, 280)

square = L_Square(300, 300, 50)

line = L_Line()
line.setNextVertex(100, 200)
line.setNextVertex(300, 400)


import math
def rotatePolygon(polygon,theta):
    """Rotates the given polygon which consists of corners represented as (x,y),
    around the ORIGIN, clock-wise, theta degrees"""
    theta = math.radians(theta)
    rotatedPolygon = []
    for corner in polygon :
        rotatedPolygon.append(( corner[0]*math.cos(theta)-corner[1]*math.sin(theta) , corner[0]*math.sin(theta)+corner[1]*math.cos(theta)) )
    return rotatedPolygon


my_polygon = [(0,0),(1,0),(0,1)]
print rotatePolygon(my_polygon,90)


def main():

	
    win = GraphWin("My Circle", 500, 500)

    # c = Circle(cir.getPointCenter(), cir.radius)
    # c.setFill(cir.getColor())
    # c.draw(win)

    # t = Polygon(triangle.getPointsList())
    # t.setFill(triangle.getColor())
    # t.draw(win)


    p = Polygon(ply.getPointsList())
    p.setFill(ply.getColor())
    p.draw(win)

    # r = Rectangle(rect.getPoints())
    # r.draw(win)

    # s = Rectangle(square.getPoints())
    # s.draw(win)

    # l = Line(line.getPoints())


    # l.draw(win)

    # t = Text(Point(300, 300), "Hello darkness my old friend")
    # t.setFill(color_rgb(255, 255, 255))
    # t.draw(win)
    # t.undraw()
    # time.sleep(2)
    # t.draw(win)

    win.setBackground(color_rgb(50, 20, 50))


    # p = Polygon(Point(100,100), Point(500,300), Point(200,400))
    # p.draw(win)

    # 
    # for i in range(0, 100):
    # 	#print(i)
    # 	c.move(1, 1)
    # 	time.sleep(0.05)
    # 	#win.getMouse()



    win.getMouse() # Pause to view result
    win.close()    # Close window when done

main()