from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
snake.move()
        

# snake
# food
# scoreboard


# tim = Turtle()
# print(tim)


screen.exitonclick()