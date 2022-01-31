# 1. import turtle.py
import turtle
import math
# 2. create a screen object
screen = turtle.Screen()

# 3. create a turtle(pen) object
t = turtle.Turtle()
t.shape()


def draw_star(length, star_corner_angle):
    angle = 180-star_corner_angle
    for i in range(19):
        t.forward(length) 
        t.right(angle)
        length+=10

star_longest_side_len = 10

# star angle in 5 angles
star_corner_angle = 180//5

t.left(225)

draw_star(star_longest_side_len,star_corner_angle)

screen.exitonclick()

# reference:
# https://mindyourdecisions.com/blog/2018/12/03/what-is-the-sum-of-angles-in-a-star-challenge-from-india/
