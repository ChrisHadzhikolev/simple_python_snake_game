import random as rand
from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

turtleObj = Turtle("square")
turtleObj.color("white")
turtleObj.penup()

turtleObj1 = Turtle("square")
turtleObj1.color("white")
turtleObj1.penup()
turtleObj1.setposition(turtleObj.xcor()-20, turtleObj.ycor())

def new_segment(x_cord, y_cord):
    new_turtle = Turtle("square")
    new_turtle.color("white")
    new_turtle.penup()
    new_turtle.setposition(x_cord-20, y_cord)


def up():
    pass
def down():
    pass
def right():
    pass
def left():
    pass

screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(right, "Right")
screen.onkey(left, "Left")

start_game = False
screen.exitonclick()
