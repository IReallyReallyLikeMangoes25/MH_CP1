# MH 2nd turtle race practice

# import libraries
import turtle
import random

# set all turtles/finish line
red = turtle.Turtle()
orange = turtle.Turtle()
yellow = turtle.Turtle()
green = turtle.Turtle()
blue = turtle.Turtle()
purple = turtle.Turtle()
pink = turtle.Turtle()
finish = turtle.Turtle()
win = turtle.Turtle()

win.penup()
win.goto(400, 300)

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

turtles = [red, orange, yellow, green, blue, purple, pink]

# set screen size
screen = turtle.Screen()
screen.setup(1200, 800)
screen.title("Turtle Racing")

# cursor draws line at end of screen, this is the finish line

finish.penup()
finish.goto(550, 400)
finish.right(90)
finish.pensize(10)
finish.pendown()
finish.forward(800)
# five turtles begin at the start of the screen
# all turtle start moving towards the end of the screen
# once the finish line is touched all turtles stop and display whichever turtle won
while True:
    for i in turtles:
        i.forward(random.randint(1, 50))
        if i.ycor() == 550:
            win.pendown()
            win.write("We have a winner!", font = ("Comic Sans MS", 20, "normal"))
            break

turtle.done()