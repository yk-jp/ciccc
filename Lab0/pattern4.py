# 1. import turtle.py
import turtle
import math
# 2. create a screen object
screen = turtle.Screen()

# 3. create a turtle(pen) object
t = turtle.Turtle()
t.shape("turtle")

def draw_triangle(length):

    for count in range(6):
        direction_angle = count*60
        t.setheading(direction_angle)
        for i in range(3):      
            t.forward(length)
            t.left(120)

triangle_side_len = 100
draw_triangle(triangle_side_len)

screen.exitonclick()