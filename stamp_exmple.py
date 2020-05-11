#We can send our turtles out and have them 'stamp' the canvas with their shapes. Use .stamp() on the end of their name to do this.
#Yes you can change the color of the window!
import turtle

window = turtle.Screen()
window.bgcolor("yellow")

tina = turtle.Turtle()
molly = turtle.Turtle()
george = turtle.Turtle()
wilson = turtle.Turtle()

tina.penup()
molly.penup()
george.penup()
wilson.penup()

tina.forward(100)
tina.color("black")
tina.stamp()
tina.backward(100)

molly.left(60)
molly.color("purple")
molly.forward(100)
molly.stamp()
molly.backward(100)

george.left(40)
george.color("blue")
george.forward(100)
george.stamp()
george.backward(100)

wilson.left(20)
wilson.color("green")
wilson.forward(100)
wilson.stamp()
wilson.backward(100)