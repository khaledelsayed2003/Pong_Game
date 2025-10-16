from turtle import Screen, Turtle
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

paddle_right = Paddle((350, 0))
paddle_left = Paddle((-350, 0))


screen.listen()
screen.onkey(fun= paddle_right.move_up, key="Up")
screen.onkey(fun= paddle_right.move_down, key="Down")
screen.onkey(fun= paddle_left.move_up, key="w")
screen.onkey(fun= paddle_left.move_down, key="s")


game_is_on = True
while game_is_on:
    screen.update()




























screen.exitonclick()