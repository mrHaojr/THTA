import math
import random
from turtle import *
screensize(500, 500)


def _rand_color(n: int):
    chars = '0123456789ABCDEF'
    return ['#'+''.join(random.sample(chars, 6)) for _ in range(n)][random.randint(0, n - 1)]


def _fw(w: int):
    penup()
    forward(w)
    pendown()


def _goto(x, y):
    hideturtle()
    penup()
    goto(x, y)
    pendown()
    showturtle()


if __name__ == '__main__':
    hideturtle()
    done()
