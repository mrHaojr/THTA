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


def rand_color(n: int):
    chars = '0123456789ABCDEF'
    return ['#'+''.join(random.sample(chars, 6)) for _ in range(n)][random.randint(0, n - 1)]


def draw_circle(x: float, y: float, r: int):
    _goto(x, y)
    penup()
    forward(r)
    right(90)
    pendown()
    circle(r)
    left(90)


def draw_circle_2(x: float, y: float, r: int):
    _goto(x, y)
    setheading(90)
    penup()
    forward(-r)
    pendown()
    setheading(0)
    circle(r)


def draw_shape_1(x: float, y: float, r: int):
    _goto(x, y)
    dot(10, "red")
    pensize(3)
    for i in range(12):
        color(rand_color((i+1)*2))
        draw_circle(0, 0, r/2)
        right(360/12)
    color(rand_color(30*2))
    draw_circle_2(0, 0, r/2)
    color(rand_color(30*2))
    draw_circle_2(0, 0, r)


def draw_start(x: float, y: float, width: int):
    color("black")
    _goto(x, y)
    fillcolor("yellow")
    begin_fill()
    for _ in range(5):
        forward(width)
        right(144)
    end_fill()


def draw_shape_2(x: float, y: float, r: int):
    _goto(x, y)
    dot(r*2, "red")
    for _ in range(10):
        penup()
        forward(r)
        pendown()
        right(36)
        draw_start(pos()[0], pos()[1], r)
        right(-36)
        penup()
        forward(-r)
        pendown()
        right(36)


if __name__ == '__main__':
    # draw_shape_1(0, 0, 120)
    draw_shape_2(0, 0, 120)
    hideturtle()
    done()
