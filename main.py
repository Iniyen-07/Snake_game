from turtle import Screen
import time
from snake import Snake
from fooddot import Food
from scoreboard import scoreboard
screen=Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)
position=[(0,0),(-20,0),(-40,0)]
objects=[]

snake=Snake()
food=Food()
score=scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
game=True
while game:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    #collision with food
    if snake.head.distance(food)<20:
        food.random_food()
        snake.extend()
        score.score_counter()

    #collision with wall
    if snake.head.xcor()>380 or snake.head.xcor()<-380 or snake.head.ycor()>380 or snake.head.ycor()<-380:
        game=False
        score.wall()

    #with tail
    for obj in snake.objects[1:]:
        if snake.head.distance(obj)<10:
            game=False
            score.wall()





















screen.exitonclick()
