from wall import Wall
import turtle as t
import time
from scoreboard import Scoreboard
from snake import Snake
from food import Food
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
screen = t.Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, startx=0, starty=0)
screen.bgcolor('black')
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
wall = Wall()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True


while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend_snake()

    #Detect collision with wall
    for wall_segment in wall.wall_segments:
        if snake.head.distance(wall_segment) < 20:
            scoreboard.reset_scoreboard()
            snake.reset_snake()

    #Detect collision with tail
    for segment in snake.snake_segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset_scoreboard()
            snake.reset_snake()

screen.exitonclick()
