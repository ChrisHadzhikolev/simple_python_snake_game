from turtle import Screen
import time

from scoreboard import Scoreboard
from food import Food
from snake import Snake

# setting up screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()


def game():
    # objects for snake, food and scoreboard
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    # event listeners for snake movement
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.left, "Left")

    start_game = True
    while start_game:
        # sleeping to animate snake movement
        screen.update()
        time.sleep(0.1)
        snake.move_forward()

        # if snake moves through food
        if snake.head.distance(food) < 15:
            food.move_food()
            snake.extend()
            scoreboard.score_point()

        # if snake bumps into wall
        if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() < -300 or snake.head.ycor() > 300:
            start_game = False
            scoreboard.game_over()

        # if snake bumps into it's tail
        for segment in snake.segments:
            if segment == snake.head:
                pass
            elif snake.head.distance(segment) < 10:
                start_game = False
                scoreboard.game_over()


game()
screen.exitonclick()
