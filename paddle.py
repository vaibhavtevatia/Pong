from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape('square')
        self.shapesize(stretch_wid= 5, stretch_len=1)
        self.goto(position)

    def move_up(self):
        y = self.ycor() + 20
        self.goto(self.xcor(), y)
    def move_down(self):
        y = self.ycor() - 20
        self.goto(self.xcor(), y)
