# 1. import turtle.py
import turtle
import math
# 2. create a screen object
screen = turtle.Screen()

# 3. create a turtle(pen) object
t = turtle.Turtle()
t.speed(10)
def draw_shapes_multiple_times(center_radius,length,times=22):
    for count in range(1,times):
        t.penup()
        t.goto(0,0)
        # move to the point from center 
        direction_angle = count*35
        t.forward(center_radius + length)
        t.pendown()
        t.setheading(direction_angle)
        draw_circle(length)

def draw_circle(length):
       t.circle(length)

radius_center_circle = 20
radius_middle_circle = radius_center_circle * 2
radius_outer_circle =  radius_middle_circle * 2

screen.colormode(255)
inner_circle_color_pattern = (255,20,147)
t.pencolor(inner_circle_color_pattern)
draw_shapes_multiple_times(radius_center_circle,radius_middle_circle)

outer_circle_color_pattern = (220,20,60)
t.pencolor(outer_circle_color_pattern)
draw_shapes_multiple_times(radius_center_circle,radius_outer_circle)

screen.exitonclick()
# reference 
# https://www.w3schools.com/colors/color_tryit.asp?hex=FF1493
# https://www.w3schools.com/colors/color_tryit.asp?color=Crimson