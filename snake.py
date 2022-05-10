"""
Juego: Paint

Programador 1: Daniel Alejandro Martinez Rosete
Programador 2: Andrés

Fecha:10/05/22

"""

from random import randrange
from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, 10)
counter = vector(0, 0)


def change(x, y):
    """Change snake direction. jjjj"""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries mmmm."""
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)
    counter.x += 1

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)
    clear()

    if counter.x % 5 == 0:
        if -200 < food.x < 190:
            food.x += randrange(-1, 2) * 10
        elif food.x == -200:
            food.x += 50
        elif food.x == 190:
            food.x -= 50

        if -200 < food.y < 190:
            food.y += randrange(-1, 2) * 10
        elif food.y == -200:
            food.y += 50
        elif food.y == 190:
            food.y -= 50


    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
