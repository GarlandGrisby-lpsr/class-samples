# myFractalTemplate.py
 
import turtle
 
def makeSquare(myTurtle, side):
        r = turtle.Turtle()
	r.forward(side)
	r.left(90)
	r.forward(side)
	r.left(90)
	r.forward(side)
	r.left(90)
	r.forward(side)
 
# make our turtle
squeak = turtle.Turtle()
 
# squeak makes squares centered at the same point
# but going in a slightly rotated position with each loop
# and with a slightly smaller side length each time
length = 100
while length > 0:
        makeSquare(squeak, length)
# rotate and make the sides shorter
        squeak.right(5)
        length = length - 1
 
# wait to exit until I've clicked
turtle.exitonclick()

