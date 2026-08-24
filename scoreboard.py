from turtle import Turtle
class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,350)
        self.hideturtle()
        self.update_score()
    def update_score(self):
        self.write(f"Score = {self.score}", align="center", font=("Courier", 24, "normal"))
    def score_counter(self):
        self.score+=1
        self.clear()
        self.update_score()

    def wall(self):
        self.goto(0,0)
        self.write("Game over",align="center",font=("Courier", 24, "normal"))


