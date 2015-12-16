import turtle

marmar = turtle.Turtle()

mar = 0
while mar < 40:
		turtle.colormode(255)
		marmar.color(235, 101, 252)
		marmar.right(30)
		marmar.pu()
		marmar.color(1, 252, 101)
		marmar.forward(10)
		marmar.pd()
		marmar.forward(50)
		marmar.left(80)
		marmar.forward(60)
		mar = mar - 1
turtle.exitonclick()
