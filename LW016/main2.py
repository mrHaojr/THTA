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


def draw_shape(n: int, d: int):
    setheading(-90)
    d1 = d*math.sqrt(2*(1-math.cos(2*math.pi/3)))
    _goto(-d1, d1/2)
    pensize(2)
    for _ in range(n):
        color(rand_color(1000))
        forward(d1)
        left(120)
        for _ in range(2):
            forward(d)
            right(60)
            forward(d)
            right(120)
        right(120)
        left(360/n)


if __name__ == '__main__':
    draw_shape(8, 50)
    hideturtle()
    done()
