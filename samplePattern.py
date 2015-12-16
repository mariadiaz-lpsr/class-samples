import turtle 

def makeTriangle(myTurtle, side):
	kipp.forward(side)
	kipp.left(120)
	kipp.forward(side)
	kipp.left(120)
	kipp.forward(side)
	kipp.left(120)

# make our turtle 
kipp = turtle.Turtle()
kipp.forward(150)
kipp.right(180)
# kipp makes triangles centered at a point that shifts 
# and decreases in size with each loop
length = 100
while length > 0:
	makeTriangle(kipp, length)
	kipp.forward(3)

	length = length - 1
