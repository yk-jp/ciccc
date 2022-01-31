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
        t.forward(length)
        t.left(90)

square_side_len = 200
# draw square on the left side
draw_square(square_side_len)

outer_square_start_point_moveX = square_side_len // 2
outer_square_start_point_moveY = outer_square_start_point_moveX

t.penup()
t.goto(outer_square_start_point_moveX,outer_square_start_point_moveY)

t.pendown()
# draw square on the right side
draw_square(square_side_len)

# 4. exitonclick() on your screen object
screen.exitonclick()