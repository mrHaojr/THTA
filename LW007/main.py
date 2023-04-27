import math
import random
from turtle import *
screensize(500, 500)


def _goto(x, y):
    hideturtle()
    penup()
    goto(x, y)
    pendown()
    showturtle()


def draw_one(x: float, y: float):
    forward(50 * 2)
    right(60)
    forward(30 * 2)
    right(60)
    forward(20 * 2)
    right(60)
    forward(30 * 2)
    right(60)
    forward(50 * 2)


def rand_color(n: int):
    chars = '0123456789ABCDEF'
    return ['#'+''.join(random.sample(chars, 6)) for _ in range(n)][random.randint(0, n - 1)]


def draw_shape(x: float, y: float):
    n = 24
    pensize(3)
    for i in range(n):
        color(rand_color(i + 1))
        draw_one(x, y)
        right(360/n)


if __name__ == '__main__':
    draw_shape(0, 0)
    hideturtle()
    done()
