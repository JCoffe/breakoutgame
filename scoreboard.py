from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(-300,260)
        self.write(self.score, align="center", font=("Courir", 30, "normal"))
        self.updatescoreboard()


    def updatescoreboard(self):
        self.clear()
        self.goto(-300, 260)
        self.write(self.score, align="center", font=("Courir", 30, "normal"))


    def redscore(self):
        self.score += 50
        self.updatescoreboard()


    def bluescore(self):
        self.score += 20
        self.updatescoreboard()
