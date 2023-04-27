import math
import random
from turtle import *
screensize(500, 500)


def rand_color(n: int):
    chars = '0123456789ABCDEF'
    return ['#'+''.join(random.sample(chars, 6)) for _ in range(n)][random.randint(0, n - 1)]


def _goto(x, y):
    hideturtle()
    penup()
    goto(x, y)
    pendown()
    showturtle()


def draw_one():
    r = 5
    pensize(2)
    right(90)
    for _ in range(16):
        for _ in range(3):
            forward(r)
            right(360 / 6)
        r += 5
    left(90)


def draw_shape(n: int):
    setheading(-90)
    _goto(0, 0)
    for _ in range(n):
        x, y = pos()[0], pos()[1]
        draw_one()
        _goto(x, y)
        left(90)
        forward(80)
        right(90)
        right(360 / n)


if __name__ == '__main__':
    draw_shape(2)
    hideturtle()
    done()
