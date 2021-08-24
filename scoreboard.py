from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.write_score()
        self.goto(0, 270)
        self.color("white")
        self.write(align="center", arg=f"Score: {self.score}", font=("Times New Roman", 15, "normal"))
        self.penup()
        self.ht()

    def score_point(self):
        self.score += 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(align="center", arg=f"Score: {self.score}", font=("Times New Roman", 15, "normal"))

    def game_over(self):
        game_over = Turtle()
        game_over.color("white")
        game_over.write(align="center", arg="Game Over.", font=("Times New Roman", 15, "normal"))
