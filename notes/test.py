import turtle

def border():
    # turtle draws a border around all squares
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.forward(180)
    turtle.right(90)
    turtle.forward(180)
    turtle.right(90)
    turtle.forward(180)
    turtle.right(90)
    turtle.forward(180)

border()

