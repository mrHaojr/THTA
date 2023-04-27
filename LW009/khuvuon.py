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


def draw_shape(x: float, y: float, r: int, n: int):
    _goto(x, y)
    pensize(2)
    for i in range(1, n + 1):
        for _ in range(i):
            fillcolor("yellow")
            begin_fill()
            for _ in range(4):
                forward(r)
                right(90)
            end_fill()
            forward(r)
        if (i != n):
            forward(-r*i)
            setheading(-90)
            forward(r)
            setheading(0)
            forward(-r/2)


if __name__ == '__main__':
    r = 20
    n = int(input("Nhap so hang: "))
    draw_shape(0 - r//2, 300, r, n)
    hideturtle()
    done()
