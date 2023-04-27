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


def draw_leaf(x: float, y: float, r: int):
    _goto(x, y)
    pensize(3)
    right(45)
    begin_fill()
    circle(r, 90)
    _goto(x, y)
    right(180)
    circle(r, -90)
    end_fill()
    _goto(x, y)
    right(135)


def draw_flower_1(x: float, y: float, r: int, n: int):
    for i in range(n):
        color(rand_color((i+1)*10))
        draw_leaf(x, y, r)
        right(360 / n)
    dot(r, "yellow")


def draw_N(x: float, y: float, r2: int, n: int):
    _goto(x, y)
    setheading(90)
    pensize(3)
    r = r2/math.sqrt((1-math.cos(2*math.pi / n))*2)
    angle1 = 360/n
    angle2 = 180 - (180 - angle1) / 2
    r3 = r/3
    for _ in range(n):
        penup()
        forward(r)
        pendown()
        right(angle2)
        forward(r2)
        forward(-r2)
        left(angle2)
        forward(-r3)
        draw_flower_1(pos()[0], pos()[1], 25, 5)
        penup()
        forward(-(r-r3))
        pendown()
        right(angle1)


if __name__ == '__main__':
    r = 25
    # draw_flower_1(0, 0, 25)
    draw_N(0, 0, 110, 10)
    hideturtle()
    done()
