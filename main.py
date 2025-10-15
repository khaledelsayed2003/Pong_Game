from turtle import Screen, Turtle, width


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)


paddle_1 = Turtle()
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(350, 0)


def move_up():
    new_y = paddle_1.ycor() + 20
    paddle_1.goto(paddle_1.xcor(), new_y)
    

def move_down():
    new_y = paddle_1.ycor() - 20
    paddle_1.goto(paddle_1.xcor(), new_y)
    
    

screen.listen()
screen.onkey(fun= move_up, key="Up")
screen.onkey(fun= move_down, key="Down")


game_is_on = True
while game_is_on:
    screen.update()





























screen.exitonclick()