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


def draw_leaf():
    circle(50, 90)
    circle(50, -90)
    right(90)
    circle(50, -90)
    circle(50, 90)
    left(90)


def draw_flower(n: int, rTron: int, d: int):
    r = 180 + 360/n
    # r = 360 - (90 - 360/n)*2 - 360/n
    pensize(2)
    setheading(180)
    for _ in range(n):
        _goto(0, rTron*2)
        circle(rTron, -r)
        left(r)
        right(360/n)
    setheading(-90)
    _goto(0, 0)
    pensize(3)
    forward(d)
    _goto(0, -d/2)
    right(270)
    draw_leaf()
    _goto(0, -d/1.5)
    right(270)
    draw_leaf()


if __name__ == '__main__':
    draw_flower(20, 40, 150)
    hideturtle()
    done()
