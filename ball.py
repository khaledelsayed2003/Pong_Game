from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        
        
    def move_up_right(self):
        new_x = self.xcor() + 13
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)

        
        