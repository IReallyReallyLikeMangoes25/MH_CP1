# Mh libraries notes

import turtle
import random

turtle.shape("turtle")
turtle.color("#a9d660")
turtle.pensize(20)
turtle.fillcolor("#CF8641")
turtle.begin_fill()
for x in range(4):
    turtle.forward(250)
    turtle.right(90)
turtle.end_fill()



turtle.penup()
turtle.goto(-50, 100)
turtle.pendown()
turtle.color("#a9d660")
turtle.pensize(20)
turtle.fillcolor("#CF8641")
turtle.begin_fill()
for x in range(4):
    turtle.forward(250)
    turtle.right(90)
turtle.end_fill()

turtle.done()