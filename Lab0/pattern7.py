# 1. import turtle.py
import turtle
import math
# 2. create a screen object
screen = turtle.Screen()

# change bg color to green
screen.bgcolor("green")

# 3. create a turtle(pen) object
t = turtle.Turtle()
t.shape("turtle")

# change turtle color
t.color("blue")

def draw_circle(length, angle):
    for i in range(12):
      # rotate the turtle angle counter clockwise
        t.penup()
        t.forward(length)
        t.pendown()
        t.forward(10)
        t.penup()
        t.forward(10)
        t.stamp()
        t.goto(0,0)
        t.left(angle)

radius_len = 200

turtle_movement_angle = 360//12

draw_circle(radius_len, turtle_movement_angle)

screen.exitonclick()

# reference:
# https://mindyourdecisions.com/blog/2018/12/03/what-is-the-sum-of-angles-in-a-star-challenge-from-india/
