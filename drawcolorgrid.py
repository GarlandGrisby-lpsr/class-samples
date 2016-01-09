# done on trinket.io
import turtle
t = turtle.Turtle()
t.speed(20)
def rsquare(t):
  times = 0
  while times < 4:
    t.color('red')
    t.forward(20)
    t.right(90)
    times = times + 1

def bsquare(t):
  times = 0
  while times < 4:
    t.color('blue')
    t.forward(20)
    t.right(90)
    times = times + 1

def ysquare(t):
  times = 0
  while times < 4:
    t.color('yellow')
    t.forward(20)
    t.right(90)
    times = times + 1

def gsquare(t):
  times = 0
  while times < 4:
    t.color('green')
    t.forward(20)
    t.right(90)
    times = times + 1

rsquare(t)
t.forward(20)
bsquare(t)
t.right(90)
t.forward(20)
ysquare(t)
t.left(90)
gsquare(t)
t.left(90)
t.penup()
t.forward(15)
t.pendown()

# second square
t.left(90)
gsquare(t)
t.forward(20)
ysquare(t)
t.right(90)
t.forward(20)
bsquare(t)
t.left(90)
rsquare(t)
t.right(90)
t.penup()
t.forward(15)
t.pendown()

# third square

t.left(90)
gsquare(t)
t.forward(20)
ysquare(t)
t.right(90)
t.forward(20)
bsquare(t)
t.left(90)
rsquare(t)
t.left(90)
t.penup()
t.forward(15)
t.pendown()

# fourth square

t.penup()
t.right(180)
t.forward(30)
t.left(90)
t.pendown()
gsquare(t)
t.forward(20)
ysquare(t)
t.right(90)
t.forward(20)
bsquare(t)
t.left(90)
rsquare(t)
t.left(90)
t.penup()
t.forward(15)
t.pendown()

# fifth square

t.penup()
t.right(180)
t.forward(30)
t.left(90)
t.pendown()
gsquare(t)
t.forward(20)
ysquare(t)
t.right(90)
t.forward(20)
bsquare(t)
t.left(90)
rsquare(t)
t.left(90)
t.penup()
t.forward(15)
t.pendown()
