import turtle 

def drawTee(myTurtle):
	number = 0 
	while number < 4:
		drawFourTees(myTurtle)
		number = number + 1

def drawFourTees(myTurtle):
	myTurtle.fd(40)
	myTurtle.backward(10)
	myTurtle.left(90)
	myTurtle.fd(10)
	myTurtle.backward(20)
	myTurtle.fd(10)
	myTurtle.left(90)
	myTurtle.fd(30)
	myTurtle.left(90)

glowy = turtle.Turtle()
drawTee(glowy)
turtle.exitonclick()
# make your turtle down here and pass it to the appropriate places
