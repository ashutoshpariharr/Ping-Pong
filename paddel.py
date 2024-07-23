from turtle import Turtle, Screen

screen = Screen()


class Paddel(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def set_up(self):
        y_cor = self.ycor() + 20
        self.goto(self.xcor(), y_cor)

    def set_down(self):
        y_cor = self.ycor() - 20
        self.goto(self.xcor(), y_cor)
