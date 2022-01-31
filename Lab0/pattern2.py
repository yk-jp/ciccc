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
diagonal_len = square_side_len*math.sqrt(2)  
# draw inner square
draw_square(square_side_len)

outer_square_start_point_moveX = square_side_len // 2
outer_square_start_point_moveY = (diagonal_len - square_side_len)//2

t.penup()
t.goto(outer_square_start_point_moveX,-outer_square_start_point_moveY)

# rotate turtle 45 degree counter-clockwise
t.setheading(45)

t.pendown()
draw_square(square_side_len)

# 4. exitonclick() on your screen object
screen.exitonclick()