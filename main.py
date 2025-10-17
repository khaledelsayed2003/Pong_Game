from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)
user_input = screen.textinput(title="Welcome to the Pong game!", prompt="Pick the start speed of the game! Type '0.1' for normal speed or increase the speed by writing number less than '0.1'.")
game_speed = float(user_input)
reset_game_speed = game_speed


paddle_right = Paddle((350, 0))
paddle_left = Paddle((-350, 0))
ball = Ball()
score_r = Score(300, 200)
score_l = Score(-300, 200)


screen.listen()
screen.onkey(fun= paddle_right.move_up, key="Up")
screen.onkey(fun= paddle_right.move_down, key="Down")
screen.onkey(fun= paddle_left.move_up, key="w")
screen.onkey(fun= paddle_left.move_down, key="s")



game_is_on = True
while game_is_on:
    time.sleep(game_speed)
    screen.update()
    ball.move_up_right()
    
    #Detect collision with wall
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()
        
        
    #Detect collision with paddle_right & increase ball speed
    if ball.distance(paddle_right) < 50 and ball.xcor() > 330:
        ball.bounce_x()
        game_speed *= 0.9
    
    #Detect collision with paddle_left & increase ball speed
    if ball.distance(paddle_left) < 50 and ball.xcor() < -330:
        ball.bounce_x()    
        game_speed *= 0.9
        
    #Detect when the Ball goes out of the bounds (paddle_right) & update scores & reset speed:
    if ball.xcor() > 380:
        game_speed = reset_game_speed
        score_l.refresh()
        ball.reset_position()
    #Detect when the Ball goes out of the bounds (paddle_left) & update scores & reset speed:
    if ball.xcor() < -380:
        game_speed = reset_game_speed
        score_r.refresh()
        ball.reset_position()
        


    

        



























screen.exitonclick()