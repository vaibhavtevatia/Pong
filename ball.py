from turtle import Turtle
x = 10
y = 10
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('blue')
        self.penup()
        # self.start_ball()

    # def start_ball(self):
    #     self.setpos(x,y)

    def move_ball(self):
        new_x = self.xcor() + x
        new_y = self.ycor() + y
        self.goto(new_x,new_y)

    def wall_bounce(self):
        global y
        y = -y

    def paddle_bounce(self):
        global x
        x = -x
