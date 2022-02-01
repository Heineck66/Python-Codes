from turtle import Turtle, update

ALIGN = "center"
FONT = ("Arial", 16, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.load_highscore()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.score = 0
            self.update_score()
            self.save_highscore()

    def update_score(self):
        self.clear()
        self.setpos(-10, 270)
        self.write(
            f"score: {self.score}   Highscore: {self.high_score}",
            True,
            align=ALIGN,
            font=(FONT),
        )

    def increase_score(self):
        self.score += 10

    def save_highscore(self):
        data = open("data.txt", "w")
        data.write(str(self.high_score))
        data.close()

    def load_highscore(self):
        data = open("data.txt")
        highscore = data.read()
        print(highscore)
        data.close()
        return int(highscore)
