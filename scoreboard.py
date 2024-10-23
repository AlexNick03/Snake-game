from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 20, 'normal')

file_r = open("data.txt", "r")
HIGH_SCORE_VALUE = int(file_r.read())
file_r.close()


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = HIGH_SCORE_VALUE
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.color('white')
        self.update_scoreboard()

    def reset_scoreboard(self):

        if self.score > self.high_score:
            my_file = open("data.txt", "w")
            self.high_score = self.score
            my_file.write(str(self.score))
            my_file.close()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score} High Score = {self.high_score}", align="center", font=("Courier", 20, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
