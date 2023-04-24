from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkeypress(snake.up, 'w')
screen.onkeypress(snake.left, 'a')
screen.onkeypress(snake.down, 's')
screen.onkeypress(snake.right, 'd')

food = Food()
scoreboard = ScoreBoard()

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    x_wall = snake.head.xcor() > 280 or snake.head.xcor() < -280
    y_wall = snake.head.ycor() > 280 or snake.head.ycor() < -280

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.rand_pos()
        scoreboard.increase_score()
        snake.extend()

    # Detect collision with walls
    if x_wall or y_wall:
        scoreboard.reset_score()
        snake.reset_snake()

    # Detect collision with tail
    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset_score()
            snake.reset_snake()

screen.exitonclick()
