# MH 2nd maze practice

import turtle
import random

screen = turtle.Screen()
screen.setup(180, 180)
screen.title("Maze generator")

# sets 36 squares
squares = [[0, 0], [0, 30], [0, 60], [0, 90], [0, 120], [0, 150],
           [30, 0], [30, 30], [30, 60], [30, 90], [30, 120], [30, 150],
           [60, 0], [60, 30], [60, 60], [60, 90], [60, 120], [60, 150],
           [90, 0], [90, 30], [90, 60], [90, 90], [90, 120], [90, 150],
           [120, 0], [120, 30], [120, 60], [120, 90], [120, 120], [120, 150],
           [150, 0], [150, 30], [150, 60], [150, 90], [150, 120], [150, 150]
           ]


def set_square(square_num):
    turtle.penup()
    turtle.goto(square_num)
    turtle.pendown()
    # turtle goes sqaure by square and goes to every side of every square and randomly decides if that side will be white or black:
    # turtle goes to squarework
    for i in range(1, 4):
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
        else:
            turtle.color("#FFFFFF")
            turtle.forward(30)

        turtle.right(90)



def border():
    # turtle draws a border around all squares
    turtle.goto(0,0)
    turtle.forward(180)
    turtle.right(90)
    turtle.forward(180)
    turtle.right(90)
    turtle.forward(180)
    turtle.right(90)
    turtle.forward(180)

def path():
    # turtle draws line through maze- that is the correct path:
    # turtle starts 1 square in
    turtle.penup()
    turtle.goto(30, 0)
    turtle.color("#FFFFFF")
    turtle.pendown()
    # turtle can either go 1 square forward down, left, right, or up
    # if moving forward will cause it to go too far, choose another directon
    # turtle moves 1 square forward