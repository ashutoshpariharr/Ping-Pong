from turtle import Turtle, Screen
import paddel
from ball import Ball
import time
from score_bord import Scoreboard

r_paddel = paddel.Paddel((350, 0))
l_paddel = paddel.Paddel((-350, 0))
ball = Ball()

turtle = Turtle()
screen = Screen()
score_bord = Scoreboard()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)
screen.listen()

screen.onkey(r_paddel.set_up, "Up")
screen.onkey(r_paddel.set_down, "Down")
screen.onkey(l_paddel.set_up, "s")
screen.onkey(l_paddel.set_down, "w")

is_update = True
while is_update:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    # Find a ball cordinate
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()

    # Find the distance between ball and paddel
    if ball.distance(r_paddel) < 50 and ball.xcor() > 320 or ball.distance(l_paddel) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Paddel and ball distance.
    if ball.xcor() > 380:
        ball.reset_position()
        score_bord.l_point()

    if ball.xcor() < -360:
        ball.reset_position()
        score_bord.r_point()


screen.exitonclick()




