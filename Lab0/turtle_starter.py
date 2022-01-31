# 1. import turtle.py
import turtle

# 2. create a screen object
screen = turtle.Screen()

# 3. create a turtle(pen) object
t = turtle.Turtle()
t.shape("turtle")

for i in range(4):
    t.forward(200)
    t.left(90)

# 4. exitonclick() on your screen object
screen.exitonclick()