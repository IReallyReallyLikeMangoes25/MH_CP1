# MH 2nd turtle race practice

# import libraries
import turtle
import random

# set all turtles/finish line
def setup():
    red = turtle.Turtle()
    orange = turtle.Turtle()
    yellow = turtle.Turtle()
    green = turtle.Turtle()
    blue = turtle.Turtle()
    purple = turtle.Turtle()
    pink = turtle.Turtle()
    finish = turtle.Turtle()
    win = turtle.Turtle()

    # set screen size
    screen = turtle.Screen()
    screen.setup(1200, 800)
    screen.title("Turtle Racing")

    win.speed(100)
    win.penup()
    win.goto(-150, 350)

    red.color("#FF0000")
    red.shape("turtle")
    red.penup()
    red.goto(-550, 300)
    red.pendown()
    orange.color("#FF7B00")
    orange.shape("turtle")
    orange.penup()
    orange.goto(-550, 200)
    orange.pendown()
    yellow.color("#FFE600")
    yellow.shape("turtle")
    yellow.penup()
    yellow.goto(-550, 100)
    yellow.pendown()
    green.color("#2BFF00")
    green.shape("turtle")
    green.penup()
    green.goto(-550, 0)
    green.pendown()
    blue.color("#0400FF")
    blue.shape("turtle")
    blue.penup()
    blue.goto(-550, -100)
    blue.pendown()
    purple.color("#6F00FF")
    purple.shape("turtle")
    purple.penup()
    purple.goto(-550, -200)
    purple.pendown()
    pink.color("#FF00EA")
    pink.shape("turtle")
    pink.penup()
    pink.goto(-550, -300)
    pink.pendown()
# cursor draws line at end of screen, this is the finish line

    finish.penup()
    finish.goto(550, 400)
    finish.right(90)
    finish.pensize(10)
    finish.pendown()
    finish.forward(800)

    return red, orange, yellow, green, blue, purple, pink

# five turtles begin at the start of the screen
# all turtle start moving towards the end of the screen
def move(turtle):
    turtle.forward(random.randint(1,25))

# once the finish line is touched all turtles stop and display whichever turtle won

def win(turtle, xcor):
    if xcor >= 550:
        message = f"{turtle} wins!"
        win == True
        return win, message
    else:
        win == False
        return win


red, orange, yellow, green, blue, purple, pink = setup()


while True:
    move(red)
    if win("red", red.xcor()) == False



turtle.done()