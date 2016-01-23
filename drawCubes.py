import turtle

def drawRhombus(myTurtle):
		draw = 0
# it will turn into a 30 degree angle 
		myTurtle.left(30)
	# this is making a while loop to make the rhombus top part
		while draw < 4:
# it will begin the fill with light green for the rhombus while making the shape 
			myTurtle.fillcolor("light green")
			myTurtle.begin_fill()
			myTurtle.fd(20)
			myTurtle.left(120)
			myTurtle.fd(20)
			myTurtle.left(60)
# this will end the light green color fill
			myTurtle.end_fill()
			draw = draw + 1
# it will make it turn right 120 
		myTurtle.right(120)
		myTurtle.fd(20)
		myTurtle.left(90)
		ha = 0
		myTurtle.left(90)
		while ha < 4:
# it is going to start a fill of color of light blue1 
			myTurtle.fillcolor("LightBlue1")
			myTurtle.begin_fill()
			myTurtle.fd(20)
			myTurtle.left(60)
			myTurtle.fd(20)
			myTurtle.left(120)
			myTurtle.end_fill()
			ha = ha + 1
# this will make the misty rose color at the right side
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
# this is the part where it will make the 3d shape figure  
def draw3DCubes(myTurtle):
		number = 0 
		while number < 4:
# cubes will be made under the rhombus 
			drawRhombus(myTurtle)
			myTurtle.pu()
# its going to turn right 30 forward and left to make a cube 			
			myTurtle.right(30)
			myTurtle.fd(20)
			myTurtle.left(30)
			myTurtle.pd()
			number = number + 1 
# this defines that we are going to make the cubes into 15 rows
def drawRows(myTurtle):
	josh = 0
	while josh < 15:
		draw3DCubes(myTurtle)
# turtle is going to pen up and make rows in a specific shape to make it go all the way next where the first cube was made  
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
# turtle name is ocean 
ocean = turtle.Turtle()	
drawRows(ocean)
turtle.exitonclick()
				
