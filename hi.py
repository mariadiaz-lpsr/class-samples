
import turtle

addition = turtle.Turtle()

sign = 0

while sign < 7:
        addition.color("red")
        addition.forward(300)
        addition.back(150)
        addition.left(90)
        addition.forward(150)
        addition.back(150)
        addition.right(180)
        addition.forward(150)
        sign = sign + 1
        turtle.exitonclick()

