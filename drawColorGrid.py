import turtle

def drawSideSquare(myTurtle):
		length = 0
		while length < 2:
			drawFigure(myTurtle)
			length = length + 1


def drawFigure(myTurtle):
		myTurtle.color('red')
		drawSquare(myTurtle)
		myTurtle.right(90)
		myTurtle.color('yellow')
		drawSquare(myTurtle)
		myTurtle.right(90)
		myTurtle.color('blue')
		drawSquare(myTurtle)
		myTurtle.right(90)
		myTurtle.color('green')
		drawSquare(myTurtle)
		myTurtle.right(90)
def drawSquare(myTurtle):
	square = 0
	while square < 4:
		myTurtle.fd(20)
		myTurtle.left(90)
		square = square + 1

life = turtle.Turtle()	
side = 0
while side < 5:
	drawSideSquare(life)
	life.pu()
	life.fd(20)
	life.right(90)
	life.fd(12)
	life.pd()
	life.fd(20)
	life.left(90)
	side = side + 1
turtle.exitonclick()
