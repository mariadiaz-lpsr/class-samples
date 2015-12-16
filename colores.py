import turtle

marmar = turtle.Turtle()

color = 0
marmar.speed(150)
while color < 400:
        turtle.colormode(255)
        marmar.color(235, 101, 252)
        marmar.forward(50)
        marmar.right(90)
        marmar.color(1, 252, 101)
        marmar.forward(50)
        marmar.left(100)
        marmar.color(235, 245, 42)
        marmar.right(53)
        marmar.forward(50)
        marmar.pu()
        marmar.fd(50)
        marmar.pd()
        marmar.pu()
        marmar.color(33, 11, 227)
        marmar.fd(50)
        marmar.left(90)
        marmar.pd()  
	marmar.fd(50)
        marmar.left(40)
        color = color + 1
turtle.exitonclick()

 
