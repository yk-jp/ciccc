# 1. import turtle.py
import turtle

# 2. create a screen object
screen = turtle.Screen()

# 3. create a turtle(pen) object
t = turtle.Turtle()
t.shape("turtle")

# YOUR CODE GOES HERE...


def draw_square(length):
    for i in range(4):
        t.forward(length)
        t.left(90)


draw_square(200)
t.penup()
t.goto(-50, -50)
t.pendown()
draw_square(300)

# 4. exitonclick() on your screen object
screen.exitonclick()