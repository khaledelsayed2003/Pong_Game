from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

paddle_right = Paddle((350, 0))
paddle_left = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(fun= paddle_right.move_up, key="Up")
screen.onkey(fun= paddle_right.move_down, key="Down")
screen.onkey(fun= paddle_left.move_up, key="w")
screen.onkey(fun= paddle_left.move_down, key="s")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move_up_right()
    
    #Detect collision with wall
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()
        
        
    #Detect collision with paddle_right
    if ball.distance(paddle_right) < 50 and ball.xcor() > 330:
        ball.bounce_x()
    
    #Detect collision with paddle_left
    if ball.distance(paddle_left) < 50 and ball.xcor() < -330:
        ball.bounce_x()    
        
    #Detect when the Ball goes out of the bounds (paddle_right)
    if ball.xcor() > 380:
        ball.reset_position()
    #Detect when the Ball goes out of the bounds (paddle_left)
    if ball.xcor() < -380:
        ball.reset_position()
        


    

        



























screen.exitonclick()