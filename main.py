from turtle import Screen, Turtle
from block import Block
from ball import Ball
from scoreboard import Scoreboard
import time

#Initialize
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("BreakoutGAME")
screen.tracer(0)

paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(x=0, y=-250)
ball1 = Ball()
scoreboard = Scoreboard()
def go_left():
    new_x = paddle.xcor() - 50
    paddle.goto(new_x, paddle.ycor())


def go_right():
    new_x = paddle.xcor() + 50
    paddle.goto(new_x, paddle.ycor())



block1 = Block(position=(-350, 100))
block2 = Block(position=(-250, 100))
block3 = Block(position=(-150, 100))
block4 = Block(position=(-50, 100))
block5 = Block(position=(50, 100))
block6 = Block(position=(150, 100))
block7 = Block(position=(250, 100))
block8 = Block(position=(350, 100))
block9 = Block(position=(-350, 130))
block10 = Block(position=(-250, 130))
block11 = Block(position=(-150, 130))
block12 = Block(position=(-50, 130))
block13 = Block(position=(50, 130))
block14 = Block(position=(150, 130))
block15 = Block(position=(250, 130))
block16 = Block(position=(350, 130))
block17 = Block(position=(-350, 160))
block18 = Block(position=(-250, 160))
block19 = Block(position=(-150, 160))
block20 = Block(position=(-50, 160))
block21 = Block(position=(50, 160))
block22 = Block(position=(150, 160))
block23 = Block(position=(250, 160))
block24 = Block(position=(350, 160))

block25 = Block(position=(-350, 190))
block26 = Block(position=(-250, 190))
block27 = Block(position=(-150, 190))
block28 = Block(position=(-50, 190))
block29 = Block(position=(50, 190))
block30 = Block(position=(150, 190))
block31 = Block(position=(250, 190))
block32 = Block(position=(350, 190))

block32 = Block(position=(-350, 220))
block33 = Block(position=(-250, 220))
block34 = Block(position=(-150, 220))
block35 = Block(position=(-50, 220))
block36 = Block(position=(50, 220))
block37 = Block(position=(150, 220))
block38 = Block(position=(250, 220))
block39 = Block(position=(350, 220))

block40 = Block(position=(-350, 250))
block41 = Block(position=(-250, 250))
block42 = Block(position=(-150, 250))
block43 = Block(position=(-50, 250))
block44 = Block(position=(50, 250))
block45 = Block(position=(150, 250))
block46 = Block(position=(250, 250))
block47 = Block(position=(350, 250))

screen.listen()
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")

game_on = True
while game_on:
    time.sleep(0.05)
    screen.update()
    ball1.move()

    #Detect collision with wall on the sides
    if ball1.xcor() > 350 or ball1.xcor() < -350:
        ball1.bounce_x()

    #Detect collision with paddle
    if ball1.distance(paddle) < 60 and ball1.ycor() < -230:
        ball1.bounce_y()

    #Detect collision with top wall
    if ball1.ycor() > 280:
        ball1.bounce_y()


    #Detect if ball is below bottom line
    if ball1.ycor() < -320:
        print("Ball out of bounds!!")
        ball1.goto(0,0)
        ball1.color("red")
    #Detect collision with a block

    block1.collision(ball1.position(), ball1,scoreboard)
    block2.collision(ball1.position(), ball1,scoreboard)
    block3.collision(ball1.position(), ball1,scoreboard)
    block4.collision(ball1.position(), ball1,scoreboard)
    block5.collision(ball1.position(), ball1,scoreboard)
    block6.collision(ball1.position(), ball1,scoreboard)
    block7.collision(ball1.position(), ball1,scoreboard)
    block8.collision(ball1.position(), ball1,scoreboard)

    block9.collision(ball1.position(), ball1,scoreboard)
    block10.collision(ball1.position(), ball1,scoreboard)
    block11.collision(ball1.position(), ball1,scoreboard)
    block12.collision(ball1.position(), ball1,scoreboard)
    block13.collision(ball1.position(), ball1,scoreboard)
    block14.collision(ball1.position(), ball1,scoreboard)
    block15.collision(ball1.position(), ball1,scoreboard)
    block16.collision(ball1.position(), ball1,scoreboard)

    block17.collision(ball1.position(), ball1, scoreboard)
    block18.collision(ball1.position(), ball1, scoreboard)
    block19.collision(ball1.position(), ball1, scoreboard)
    block20.collision(ball1.position(), ball1, scoreboard)
    block21.collision(ball1.position(), ball1, scoreboard)
    block22.collision(ball1.position(), ball1, scoreboard)
    block23.collision(ball1.position(), ball1, scoreboard)
    block24.collision(ball1.position(), ball1, scoreboard)

    block25.collision(ball1.position(), ball1, scoreboard)
    block26.collision(ball1.position(), ball1, scoreboard)
    block27.collision(ball1.position(), ball1, scoreboard)
    block28.collision(ball1.position(), ball1, scoreboard)
    block29.collision(ball1.position(), ball1, scoreboard)
    block30.collision(ball1.position(), ball1, scoreboard)
    block31.collision(ball1.position(), ball1, scoreboard)
    block32.collision(ball1.position(), ball1, scoreboard)

    block33.collision(ball1.position(), ball1, scoreboard)
    block34.collision(ball1.position(), ball1, scoreboard)
    block35.collision(ball1.position(), ball1, scoreboard)
    block36.collision(ball1.position(), ball1, scoreboard)
    block37.collision(ball1.position(), ball1, scoreboard)
    block38.collision(ball1.position(), ball1, scoreboard)
    block39.collision(ball1.position(), ball1, scoreboard)
    block40.collision(ball1.position(), ball1, scoreboard)
    block41.collision(ball1.position(), ball1, scoreboard)
    block42.collision(ball1.position(), ball1, scoreboard)
    block43.collision(ball1.position(), ball1, scoreboard)
    block44.collision(ball1.position(), ball1, scoreboard)
    block45.collision(ball1.position(), ball1, scoreboard)
    block46.collision(ball1.position(), ball1, scoreboard)
    block47.collision(ball1.position(), ball1, scoreboard)


print(score)




screen.exitonclick()
#TODO Paddle controlled by the user
#TODO Ball that travels, increase speed after certain level or time
#TODO Block that dissapear when hit
#TODO Walls that stay and ball bounces
#TODO Bottom of the play-field where player looses life if ball hits
#TODO Labels displaying score, lvl etc