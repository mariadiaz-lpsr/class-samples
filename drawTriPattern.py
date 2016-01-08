import turtle

def drawAngle(myTurtle):
	num = 0
	while num < 4:
		drawTree(myTurtle)
		myTurtle.pu()
		myTurtle.fd(30)
		myTurtle.pd()
		num = num + 1

def drawTree(myTurtle):
	num = 0
	while num < 3:
		myTurtle.forward(10)
		myTurtle.left(120)
		num = num + 1

trio = turtle.Turtle()
number = 0 
while number < 3:
		drawAngle(trio)
		trio.pu()
		trio.goto(0,0)
		trio.pd()
		trio.left(20)
		number = number + 1
ns = 0
trio.left(120)
while ns < 3:
		drawAngle(trio)
		trio.pu()
		trio.goto(0,0)
		trio.pd()
		trio.left(20)
		ns = ns + 1
turtle.exitonclick()
