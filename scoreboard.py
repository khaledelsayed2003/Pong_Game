from turtle import Turtle

class Score(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.score = 0
        self.color("green")
        self.hideturtle()
        self.penup()
        self.goto(x, y)
        self.write(self.score, align= "center", font=("Courier", 50, "normal"))
        
    
    
    def refresh(self):
        self.clear()    # to delete the previous score
        self.score += 1
        self.write(self.score, align= "center", font=("Courier", 50, "normal")) 
        
    