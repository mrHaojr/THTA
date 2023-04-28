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


def draw_one(r1: int, r2: int):
    _goto(0, 0)
    r = r1 + r2
    r3 = r*math.sqrt(2)/2
    penup()
    forward((r1 + r2/2))
    right(90)
    forward(-(r1 + r2/2))
    pendown()
    pensize(2)
    for _ in range(4):
        for _ in range(4):
            forward(r1)
            right(90)
        forward(r1*2 + r2)
        right(90)
    right(-90)


def draw_shape(n: int):
    right(30)
    for _ in range(n):
        draw_one(50, 40)
        right(360/n)


if __name__ == '__main__':
    draw_shape(3)
    hideturtle()
    done()
