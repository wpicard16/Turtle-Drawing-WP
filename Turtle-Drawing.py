from turtle import *

t = Turtle()

t.speed(50)
t.color('red')

for i in range(20):
    t.circle(5*i)
    t.circle(-5*i)
    t.left(i)

t.speed(30)
t.color('blue')

for i in range(20):
    t.circle(7*i)
    t.circle(-7*i)
    t.right(i)

t.color('green')

def square(size,sides):
    for i in range(200):
        t.forward(4*i)
        t.left(90)

sides = 4
square(200,sides)
       
input('press enter to exit')