from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')

class Scoreboard(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)

        self.score_text = Turtle()
        self.score_text.color('white')
        self.score_text.penup()
        self.score_text.hideturtle()
        self.score_text.setpos(0, 270)
        self.score = 0
        self.increase_score()


    def update_scoreboard(self):
        self.score_text.clear()

    
    def increase_score(self):
        self.update_scoreboard()
        self.score_text.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.score += 1


    def game_over(self):
        # self.update_scoreboard()
        self.score_text.setpos(0, 0)
        self.score_text.write(f"Game over!", align=ALIGNMENT, font=FONT)