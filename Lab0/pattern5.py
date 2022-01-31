# 1. import turtle.py
import turtle
import math
# 2. create a screen object
screen = turtle.Screen()

# 3. create a turtle(pen) object
t = turtle.Turtle()
t.shape("turtle")

def draw_square(length):
        for i in range(4):
            move_distance = length      
            if i == 0 or i == 4:
                move_distance/=2
            t.forward(move_distance)
            t.left(90)

def draw_shape(length):
    for count in range(5):
        direction_angle = 268 + (count*70)
        t.setheading(direction_angle)
        draw_square((length))
        # go backward the point of the halfway on a line.
        t.forward(length/2)
        t.left(90)


square_side_len = 100

outer_square_start_point_moveX = square_side_len // 2
outer_square_start_point_moveY = -2

t.penup()
t.goto(outer_square_start_point_moveX,outer_square_start_point_moveY)

t.pendown()
draw_shape(square_side_len)

screen.exitonclick()
