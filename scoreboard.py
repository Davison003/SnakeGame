from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 16, "bold")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.score = 0
        with open("data.txt") as hs:
            self.high_score = int(hs.read())

        self.penup()
        self.setpos(0, 270)
        self.pencolor("white")
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}    High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as hs:
                hs.write(str(self.high_score))
        self.score = 0
        self.write_score()

    def game_over(self):
        self.home()
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.write_score()
