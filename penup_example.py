#Our turtles can move around without drawing. Just add .penup() to the end of their names to do this..

import turtle

tina = turtle.Turtle()
molly = turtle.Turtle()
george = turtle.Turtle()
wilson = turtle.Turtle()

tina.penup()
molly.penup()
george.penup()
wilson.penup()

tina.forward(100)

molly.left(60)
molly.color("yellow")
molly.forward(100)

george.left(40)
george.color("blue")
george.forward(100)

wilson.left(20)
wilson.color("green")
wilson.forward(100)

turtle.done()
