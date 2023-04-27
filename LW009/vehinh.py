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


def draw_triagle(r: int):
    left(30)
    color("yellow")
    begin_fill()
    for _ in range(3):
        forward(r)
        right(360 / 3)
    end_fill()
    right(30)


def draw_shape(x: float, y: float):
    _goto(x, y)
    dot(200, "red")
    for _ in range(8):
        _goto(x, y)
        penup()
        forward(130)
        pendown()
        draw_triagle(50)
        right(360/8)


if __name__ == '__main__':
    draw_shape(0, 0)
    hideturtle()
    done()
