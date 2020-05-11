#make a Star
# Link for Turtle examples to practice
# https://michael0x2a.com/blog/turtle-examples
#https://mahajanpoojag-7355.trinket.io/an-hour-of-python#/welcome-to-python/going-deeper-with-turtle

import turtle

star = turtle.Turtle()

for i in range(10):
    star.forward(200)
    star.right(144)

turtle.done()