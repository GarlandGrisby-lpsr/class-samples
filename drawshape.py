import turtle
def drawside(myturtle):
  count = 0
  while count < 4:
    drawvee(myturtle)
    count = count + 1
  def drawvee(myturtle):
    myturtle.forward(10)
    myturtle.right(90)
    myturtle.forward(10)
    myturtle.right(90)
    
    
shawn = turtle.Turtle()
count = 0
while count < 4:
  drawside(shawn)
  shawn.right(90)
  count = count + 1
  
turtle.exitonclick()
