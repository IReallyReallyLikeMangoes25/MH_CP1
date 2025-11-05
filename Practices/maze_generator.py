# MH 2nd maze practice

import turtle
import random

screen = turtle.Screen()
screen.title("Maze generator")

# sets 36 squares
squares = [[0, 0], [0, 30], [0, 60], [0, 90], [0, 120], [0, 180],
           [30, 0], [30, 30], [30, 60], [30, 90], [30, 120], [30, 180],
           [60, 0], [60, 30], [60, 60], [60, 90], [60, 120], [60, 180],
           [90, 0], [90, 30], [90, 60], [90, 90], [90, 120], [90, 180],
           [120, 0], [120, 30], [120, 60], [120, 90], [120, 120], [120, 180],
           [180, 0], [180, 30], [180, 60], [180, 90], [180, 120], [180, 180]
           ]


def set_square(square_num):
    sides = [0, 0, 0, 0]
    turtle.penup()
    turtle.goto(square_num)
    turtle.pendown()
    # turtle goes sqaure by square and goes to every side of every square and randomly decides if that side will be white or black:
    # turtle goes to squarework
    for i in sides(0, 3):
        # turtle decides if side 1 is white/black
        # turtle goes to next side
        # decides if side 2 is white or black
        # turtle goes to next side
        # turtle decides if side 3 is white or black
        # turtle goes to next side
        # turtle decides if side 4 is white or black
        yes_or_no = random.randint(1, 2)
        if yes_or_no == 1:
            turtle.color("#000000")
            turtle.forward(30)
            sides[i] += 1
        else:
            turtle.color("#FFFFFF")
            turtle.forward(30)
            sides[i] += 2
        turtle.left(90)

    return 


def border():
    # turtle draws a border around all squares
    turtle.color("#000000")
    turtle.penup()
    turtle.goto(-30, 210)
    turtle.pendown()
    turtle.forward(240)
    turtle.right(90)
    turtle.forward(240)
    turtle.right(90)
    turtle.forward(240)
    turtle.right(90)
    turtle.forward(240)
    turtle.right(90)
    turtle.color("#FFFFFF")
    turtle.forward(30)
    turtle.penup()
    turtle.forward(210)
    turtle.right(90)
    turtle.forward(240)
    turtle.right(90)
    turtle.pendown()
    turtle.forward(30)

def solvable():
    pass

for square in squares:
    set_square(square)



border()

turtle.done()

