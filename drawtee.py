import turtle
def drawtee(t):
	t.forward(60)
        t.right(180)
        t.forward(20)
        t.left(90)
        t.forward(20)
        t.right(180)
        t.forward(40)
        t.right(180)
        t.forward(20)
        t.right(90)
        t.forward(40)
        t.right(90)
        
def drawfourtees(t):
	times = 0
	while times < 4:
		drawtee(t)
		times = times + 1


turt = turtle.Turtle()

drawfourtees(turt)


