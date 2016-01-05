import turtle
from Tkinter import *

def regular_rhombus(myTurtle, x, y, side):
	myTurtle.pu()
	myTurtle.color('purple')
	myTurtle.goto(x,y)
	myTurtle.pd()
	pat = 0
	while pat < 4:
		myTurtle.left(40)
        	myTurtle.fd(55)
	        myTurtle.left(40)
		myTurtle.fd(55)
		pat = pat + 1		                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
# create the root Tkinter window and a Frame to go in it
root = Tk()
frame = Frame(root)

# create our turtle
josh = turtle.Turtle()

# make some simple buttons
fwd = Button(frame, text='fwd', command=lambda: josh.forward(50))
left = Button(frame, text='left', command=lambda: josh.left(90))
right = Button(frame, text ='right', command =lambda: josh.right(90)) 
pu = Button(frame, text ='penup', command =lambda: josh.pu())
pd = Button(frame, text ='pendown', command =lambda: josh.pd())
rhombus = Button(frame, text ='rhombus', command =lambda: josh.rhombus())
# put it all together
fwd.pack(side=LEFT)
left.pack(side=LEFT)
right.pack(side=LEFT)
pu.pack(side=LEFT)
pd.pack(side=LEFT)
rhombus.pack(side=LEFT)
frame.pack()

turtle.exitonclick()

