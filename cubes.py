import turtle

def drawRhombus(myTurtle):
		myTurtle.speed(250)
		draw = 0
		myTurtle.left(30)
		while draw < 4:
			myTurtle.fillcolor("light green")
			myTurtle.begin_fill()
			myTurtle.fd(20)
			myTurtle.left(120)
			myTurtle.fd(20)
			myTurtle.left(60)
			myTurtle.end_fill()
			draw = draw + 1
		myTurtle.right(120)
		myTurtle.fd(20)
		myTurtle.left(90)
		ha = 0
		myTurtle.left(90)
		while ha < 4:
			myTurtle.fillcolor("LightBlue1")
			myTurtle.begin_fill()
			myTurtle.fd(20)
			myTurtle.left(60)
			myTurtle.fd(20)
			myTurtle.left(120)
			myTurtle.end_fill()
			ha = ha + 1

		idk = 0
		myTurtle.right(60)
		while idk < 2:
			myTurtle.fillcolor("misty rose")
			myTurtle.begin_fill()
			myTurtle.fd(20)
			myTurtle.left(60)
			myTurtle.fd(20)
			myTurtle.left(120)
			myTurtle.end_fill()
			idk = idk + 1
		myTurtle.right(30)
def draw3DCubes(myTurtle):
		number = 0 
		while number < 4:
			drawRhombus(myTurtle)
			myTurtle.pu()
			myTurtle.right(30)
			myTurtle.fd(20)
			myTurtle.left(30)
			myTurtle.pd()
			number = number + 1 
def drawRows(myTurtle):
	josh = 0
	while josh < 15:
		draw3DCubes(myTurtle)
		myTurtle.pu()
		myTurtle.left(150)
		myTurtle.fd(20)
		myTurtle.right(30)
		myTurtle.fd(140)
		myTurtle.left(90)
		myTurtle.fd(20)
		myTurtle.right(210)
		myTurtle.pd()
		josh = josh + 1
ocean = turtle.Turtle()	
drawRows(ocean)
turtle.exitonclick()
				
