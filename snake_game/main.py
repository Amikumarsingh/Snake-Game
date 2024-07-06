from turtle import Turtle , Screen
from snake  import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.title("My Snake Game")
screen.bgcolor("black")
screen.setup(width=600,height=600)
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")


is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    '''detecting food collision with snake.'''
    if snake.head.distance(food) < 15 :
        food.refresh()
        snake.extent()
        scoreboard.increase_score()
        
    '''detect collision with the wall'''
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor()< -280:
        scoreboard.reset()
        snake.reset()
    
    '''detect collision with the tail'''
    for segment in snake.segments[1:] :
        if snake.head.distance(segment)<10:
            scoreboard.reset()
            snake.reset()
    







screen.exitonclick()
