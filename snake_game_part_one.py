from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()

        

# snake
# food
# scoreboard


# tim = Turtle()
# print(tim)
is_game_on = True

while is_game_on:
    screen.update()
    snake.move()
    time.sleep(0.1)
    screen.listen()
    screen.onkey(snake.up, 'Up')
    screen.onkey(snake.right, 'Right')
    screen.onkey(snake.down, 'Down')
    screen.onkey(snake.left, 'Left')

screen.exitonclick()