from turtle import Turtle, Screen
import time
screen = Screen()

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

class Snake:


    def __init__(self):
        pass


    def move(self):
        
        segments = []


        for position in STARTING_POSITIONS:
            new_segment = Turtle('square')
            new_segment.color('white')
            new_segment.penup()
            new_segment.goto(position)
            segments.append(new_segment)


        is_game_on = True
        while is_game_on:
            screen.update()
            time.sleep(0.1)

            for seg_num in range(len(segments) - 1, 0, -1):
                new_x = segments[seg_num - 1].xcor()
                new_y = segments[seg_num - 1].ycor()
                segments[seg_num].goto(new_x, new_y)

            segments[0].forward(20)
            segments[0].left(90)