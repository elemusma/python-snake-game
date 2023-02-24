from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')
# high_score_read = open('data.txt', mode='r')
# contents = high_score_read.read()
# high_score_write = open('data.txt', mode='w')
# high_score_int = int(contents)

class Scoreboard(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)

        # self.score_text = Turtle()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.setpos(0, 270)
        self.score = 0
        # print(contents)
        # high_score_read = open('data.txt', mode='r')
        # contents = high_score_read.read()
        # self.high_score = contents
        # high_score_read.close()
        with open('data.txt') as data:
            self.high_score = int(data.read())
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()


    def reset(self):
        # high_score_write = open('data.txt', mode='w')
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as data:
                data.write(f"{self.high_score}")
        #     print(self.high_score)
        #     print(type(self.high_score))
        #     print(str(self.high_score))
        # print(str(self.high_score))
        # high_score_write.write(str(self.high_score))
        # high_score_write.close()
        self.score = 0
        self.update_scoreboard()


    # def game_over(self):
    #     self.setpos(0, 0)
    #     self.write(f"Game over!", align=ALIGNMENT, font=FONT)