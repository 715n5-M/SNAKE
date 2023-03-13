from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")

snake1 = Snake()
food1 = Food()
scoreboard = Score()

screen.listen()
screen.onkey(snake1.up, "Up")
screen.onkey(snake1.down, "Down")
screen.onkey(snake1.left, "Left")
screen.onkey(snake1.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.2)

    snake1.move()

    if snake1.head.distance(food1) < 15:
        food1.refresh()
        snake1.extend()
        scoreboard.increase()


    if snake1.head.xcor() > 280 or snake1.head.xcor() < -280 or snake1.head.ycor() > 280 or snake1.head.ycor() < -280:
        scoreboard.reset_s()
        snake1.reset_snake()


screen.exitonclick()