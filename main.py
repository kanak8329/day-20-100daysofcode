from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()


screen.mainloop()


# segment_1 = Turtle("square")
# segment_1.color("black")
#
# segment_2 = Turtle("square")
# segment_2.color("black")
# segment_2.goto(-20, 0)
#
#
# segment_3 = Turtle("square")
# segment_3.color("black")
# segment_3.goto(-40, 0)












