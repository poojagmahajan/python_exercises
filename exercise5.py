###Spirling star

import turtle

spiral = turtle.Turtle()

for i in range(20):
    #spiral.forward(i * 10)
    #
    spiral.forward(i * i)
    spiral.right(144)

turtle.done()