from turtle import Turtle
X_COOD = 0
Y_COOD = 260
THE_FONT = ("arial", 20, "normal")
ALIGNMENT = "center"
with open("highscore.txt") as high:
    highscore = high.read()


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(x=X_COOD, y=Y_COOD)
        self.the_score = 0
        with open("highscore.txt") as high:
            self.highscore = high.read()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"SCORE: {self.the_score}  HIGHSCORE: {self.highscore}", align=ALIGNMENT, font=THE_FONT)

    def increase_score(self):
        self.the_score += 1
        self.update_scoreboard()


    def reset(self):
        if self.the_score > int(self.highscore):
            self.highscore = self.the_score
            with open("highscore.txt", mode="w") as higher:
                higher.write(f"{self.the_score}")
        self.the_score = 0
        self.update_scoreboard()






    # def game_over(self):
    #     self.goto(x=0,y=0)
    #     self.write(arg= "GAME OVER", align=ALIGNMENT, font=THE_FONT)







