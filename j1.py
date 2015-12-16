import turtle
 
def makeSquare(myTurtle, side):
        j1.forward(90)
        j1.left(110)
        j1.forward(90)
	j1.left(60)
	j1.forward(90)
	j1.left(110)
	j1.forward(90)
	j1.left(110)
# make our turtle
j1 = turtle.Turtle()
 
# squeak makes squares centered at the same point
# but going in a slightly rotated position with each loop
# and with a slightly smaller side length each time
length = 100
while length > 0:
        makeSquare(j1, length)
# rotate and make the sides shorter
        j1.right(5)
        length = length - 1
 
# wait to exit until I've clicked
turtle.exitonclick()

