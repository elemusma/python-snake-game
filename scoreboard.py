from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)

        self.score_text = Turtle()
        self.score_text.color('white')
        self.score_text.penup()
        self.score_text.hideturtle()
        self.score_text.setpos(-25, 280)
        self.score = 0
        self.keep_score()
    
    def keep_score(self):
        self.score_text.clear()
        self.score_text.write(f"Score: {self.score}", font=('Arial', 19, 'normal'))
        self.score += 1