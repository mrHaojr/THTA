import math
import random
from turtle import *
screensize(500, 500)


def rand_color(n: int):
    chars = '0123456789ABCDEF'
    return ['#'+''.join(random.sample(chars, 6)) for _ in range(n)][random.randint(0, n - 1)]


def fw(w: int):
    penup()
    forward(w)
    pendown()


def _goto(x, y):
    hideturtle()
    penup()
    goto(x, y)
    pendown()
    showturtle()


def draw_leaf(r: int):
    pensize(2)
    color("yellow")
    fillcolor("yellow")
    for _ in range(4):
        begin_fill()
        circle(r, 90)
        right(270)
        circle(r, 90)
        end_fill()
        left(180)


def draw_shape(r: int):
    pensize(2)
    setheading(90)
    for _ in range(4):
        fw(2*r)
        left(90)
        fw(r)
        dot(2*r, "yellow")
        fw(r)
        left(90)
        fw(r)
        dot(2*r, "yellow")
        fw(-r)
        right(90)
        fw(-2*r)
        color("black")
        right(90)
        circle(r, 180)
        right(90)
        circle(r, 180)
        circle(r, -180)
        left(90)
        circle(r, -180)
        fw(-r*2)
        right(90)

    setheading(0)
    for _ in range(4):
        penup()
        forward(r)
        pendown()
        dot(r*2, "red")
        penup()
        forward(-r)
        pendown()
        right(90)
    draw_leaf(r)


if __name__ == '__main__':
    dot(10, "red")
    draw_shape(50)
    # hideturtle()
    done()
