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


def draw_tree(x: float, y: float, n: int):
    _goto(x, y)
    setheading(-90)
    pensize(10)
    color("brown")
    forward(180)
    _goto(x, y)
    setheading(90)
    pensize(3)
    for i in range(n):
        color("black")
        _goto(x, y)
        forward(100)
        dot(40, rand_color((i+1)*10))
        right(360 / n)


if __name__ == '__main__':
    n = 15
    draw_tree(0, 0, n)
    hideturtle()
    done()
