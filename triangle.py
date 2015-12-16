
import turtle

josh = turtle.Turtle()

triangle = 0
while triangle < 7:
	josh.forward(200)
	josh.left(142)
	josh.forward(256)
	josh.left(110)
	josh.right(35)
	josh.forward(262)
	josh.left(143)
	josh.forward(211)
	triangle = triangle + 1
	turtle.exitonclick()
