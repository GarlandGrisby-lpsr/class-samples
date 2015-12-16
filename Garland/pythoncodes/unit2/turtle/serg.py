import turtle
sergio = turtle.Turtle()
sergio.color("green")
lines = 0
while lines < 11:
        sergio.shape("turtle")
        sergio.forward(60)
        sergio.stamp()
        sergio.right(33)
        lines = lines + 1
num = 0
while num < 11:
        sergio.shape("triangle")
        sergio.forward(60)
        sergio.stamp()
        sergio.left(33)
        num = num + 1
turtle.exitonclick()
