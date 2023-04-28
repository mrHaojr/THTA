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


def draw_leaf(r: int):
    pensize(2)
    setheading(90)
    right(45)
    for _ in range(3):
        _goto(0, 0)
        circle(r, 90)
        _goto(0, 0)
        right(180)
        circle(r, -90)
        left(180)
        right(360/3)


def draw_shape_1(r: int):
    for i in range(5):
        draw_leaf(r+0.3*i*r)


def draw_shape_2(n: int, r: int, d: int):
    pensize(3)
    for _ in range(n):
        penup()
        forward(d)
        pendown()

        right(90)
        color(rand_color(100))
        circle(r*2)
        left(90)

        penup()
        forward(-d)
        pendown()
        right(360/n)


def draw_five(r: float):
    forward(r)
    left(180)
    for _ in range(5):
        forward(r)
        right(72)
    right(180)
    forward(-r)


def draw_shape_3(n: int, d: int):
    r = d*math.sqrt(2*(1-math.cos(math.pi/5)))
    print(r)
    _goto(0, 0)
    pensize(2)
    for _ in range(n):
        color(rand_color(100))
        forward(d)
        draw_five(r)
        forward(-d)
        right(360/n)


def draw_shape_4(n: int, d1: int, d2: int):
    pensize(2)
    for _ in range(n):
        penup()
        forward(d1 + d2)
        left(90)
        forward(d2/2)
        left(90)
        pendown()
        for _ in range(4):
            forward(d2)
            left(90)
        left(90)
        penup()
        forward(d2/2)
        left(90)
        forward(-d1-d2)
        pendown()

        right(360/n)


if __name__ == '__main__':
    draw_shape_4(8, 10, 50)
    # draw_shape_3(10, 100)
    # draw_shape_2(11, 15, 60)
    # draw_shape_1(50)
    hideturtle()
    done()
