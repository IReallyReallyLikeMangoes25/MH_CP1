# MH 2nd maze practice

import turtle
import random

screen = turtle.Screen()
screen.setup(360, 360)
screen.title("Maze generator")

# sets 36 squares
squares = [[-180, 180], [-180, 120], [-180, 60]
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
            turtle.forward(60)
        else:
            turtle.color("#FFFFFF")
            turtle.forward(60)

        turtle.left(90)



def border():
    # turtle draws a border around all squares
    turtle.penup()
    turtle.goto(-90,90)
    turtle.pendown()
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

for square in squares:
    set_square(square)

turtle.done()

