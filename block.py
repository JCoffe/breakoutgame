from turtle import Turtle
from ball import Ball
from scoreboard import Scoreboard


class Block(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("blue")
        self.shapesize(stretch_wid=1, stretch_len=4)
        self.penup()
        self.goto(position)


    def collision(self, ball_position, ballobj=Ball, scoreobj=Scoreboard):
        if self.distance(ball_position) < 50:
            ballobj.bounce_y()
            print(self.color())
            if self.color() == ('red', 'red'):
                print("second contact")
                self.goto(1000,1000)
                scoreobj.redscore()
            self.color("red")
            print(self.color())
            ballobj.color("green")
            scoreobj.bluescore()


