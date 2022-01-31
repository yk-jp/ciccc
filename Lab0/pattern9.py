# 1. import turtle.py
import turtle
import math
# 2. create a screen object
screen = turtle.Screen()

# 3. create a turtle(pen) object
t = turtle.Turtle()
t.speed(10)
def draw_shapes_multiple_times(length,corner,degree,times=10):
    for count in range(times):
        direction_angle = count*35
        t.setheading(direction_angle)
        draw_shapes(length,corner,degree)

def draw_shapes(length,corner,degree):
    for i in range(corner):      
       t.forward(length)
       t.left(degree)


side_len = 50

#decagon
decagon_len = side_len
decagon_corner = 10
decagon_degree = 360//10

# change line colors to blue
t.pencolor("blue")
draw_shapes_multiple_times(decagon_len,decagon_corner,decagon_degree,10)

# pentagon
pentagon_len = side_len*2
pentagon_corner = 5
pentagon_degree = 360//5
# change line colors to red
t.pencolor("red")
draw_shapes_multiple_times(pentagon_len,pentagon_corner,pentagon_degree,10)

screen.exitonclick()

# reference
# https://en.wikipedia.org/wiki/Decagon
# https://en.wikipedia.org/wiki/Pentagon