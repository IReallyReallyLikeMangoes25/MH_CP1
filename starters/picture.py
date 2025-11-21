# MH 2nd picture starter
import turtle

def draw_branch(length):
    if length > 5:
        for i in range(3):
            turtle.forward(length)
            draw_branch(length/3)
            turtle.back(length)
            turtle.right(60)

turtle.speed(10)
turtle.color("#A4E1E6")
turtle.penup()
turtle.goto(30, 30)
turtle.pendown()

for i in range(6):
    draw_branch(100)
    turtle.right(60)

turtle.done()