# MH 2nd maze practice

import turtle
import random

screen = turtle.Screen()
screen.title("Maze generator")

# sets 36 squares
squares = [[0, 0], [0, 30], [0, 60], [0, 90], [0, 120], [0, 150],
           [30, 0], [30, 30], [30, 60], [30, 90], [30, 120], [30, 150],
           [60, 0], [60, 30], [60, 60], [60, 90], [60, 120], [60, 150],
           [90, 0], [90, 30], [90, 60], [90, 90], [90, 120], [90, 150],
           [120, 0], [120, 30], [120, 60], [120, 90], [120, 120], [120, 150],
           [150, 0], [150, 30], [150, 60], [150, 90], [150, 120], [150, 150]
           ]

# empty list to store where square walls are as we draw them
square_walls = []

def set_square(square_num):
    turtle.speed(5)
    sides = [0, 0, 0, 0]
    turtle.penup()
    turtle.goto(square_num)
    turtle.pendown()
    # turtle goes sqaure by square and goes to every side of every square and randomly decides if that side will be white or black:
    # turtle goes to squarework
    for i in range(4):
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
            sides[i] = 1
        else:
            turtle.color("#FFFFFF")
            turtle.forward(30)
            sides[i] = 0
        turtle.left(90)

    return sides


def border():
    turtle.color("#FD0000")
    # turtle draws a border around all squares
    turtle.penup()
    turtle.goto(0, 0)
    turtle.setheading(0)
    turtle.pendown()
    for i in range(0, 4):
        turtle.forward(180)
        turtle.left(90)
    turtle.forward(150)
    turtle.color("#FFFFFF")
    turtle.forward(30)
    turtle.penup()
    turtle.goto(0, 180)
    turtle.setheading(0)
    turtle.pendown()
    turtle.forward(30)

# function to detect if the maze is solveable (unfinished)
def solveable(walls):
    # list that can remember all forks in the road for later reference
    tryable = []
    # saves what square you are currently in
    where_am_i = 0
    # automatically adds the first square to the list of tryable options
    tryable.append([where_am_i, evaluate(walls, where_am_i)])
    # while the list of tyable options has something in it, keep trying to find your way through the maze
    while len(tryable) > 0:
        pass
    # start as square zero, view tryable options
    # as a default, the solveable checker will always follow the same order of checking down, right, up, and then left
    # depending on which of those directions is available first, where am I will be changed to whatever square you move to
    # from there, the new square will be evaluated for options, and the options will be saved in tryable
    # the solveable checker will do this for every square, effectively checking for forkes, until it either 1 - Reaches the end of the maze, and breaks out of the loop, or 2 - 
    # runs into a dead end
    # in the case of a dead end, the path with be marked off of tryable, and the solveable checker will reset to wherever the last fork in the road was, and take the next path in the direction order that is available
    # if the maze turns out to unsolveable, this function will return solveable = false


# Function to evaluate a given square for possible path options
def evaluate(walls, square):
    # takes in list of deafault options
    options = [0, 0, 0, 0]
    # goes over every side of a given square
    for i in range(4):
        # if there is a wall, change the default in options, if there is no wall, leave that spot in options the same
        if walls[square][i] == 0:
            options[i] += 1
    return options

for square in squares:
    temp_square = set_square(square)
    square_walls.append(temp_square)
    # detects if square shares walls, and updates other squares walls accordingly
    if len(square_walls) - 6 > 0:
        square_walls[len(square_walls) - 7][1] = temp_square[3]
    if (len(square_walls) - 1) % 6 != 0:
        square_walls[len(square_walls) - 2][2] = temp_square[0]

start_square = square_walls[0]
end_square = square_walls[-1]

border()

# show values of all square walls
print(square_walls)

# if solveable = false:
# erase whole maze
# draw new maze
# check if solveable again
# redo these steps until a solveable maze is generated.

turtle.done()