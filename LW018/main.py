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


def draw_shape(n: int):
    _goto(0, 0)
    r = n*5
    dot(2*r, "black")
    dot(2*(r-20), "white")
    setheading(90)
    for _ in range(n):
        fw(r - 1)
        left(90)
        fw(10)
        fillcolor("black")
        begin_fill()
        right(90)
        for _ in range(4):
            forward(20)
            right(90)
        end_fill()
        left(90)
        fw(-10)
        right(90)
        fw(-r + 1)
        right(360/n)


def draw_vien(n: int):
    r = n*math.sqrt(2)/2
    left(45)
    for _ in range(4):
        fw(r)
        right(135)
        forward(n/2-n/20)
        right(90)
        forward(n/10)
        right(90)
        circle(n/4+n/10, 90)
        right(90)
        forward(n/10)
        right(90)
        forward(n/2-n/20)
        right(90)
        left(135)
        fw(-r)
        right(90)


def draw_shape_2(n: int):
    _goto(0, 0)
    pensize(2)
    setheading(90)
    draw_vien(n)
    setheading(90)
    x = n/4
    for _ in range(8):
        right(45)
        circle(x, 90)
        left(90)
        circle(x, 90)
        right(225)
        right(360/8)


def draw_shape_3(r: int):
    _goto(-r/2, r/4)
    pensize(3)
    setheading(90)
    for _ in range(3):
        fillcolor(rand_color(1000))
        begin_fill()
        right(30)
        forward(r)
        right(120)
        forward(r)
        right(150)
        circle(r, 60)
        end_fill()

        right(150)
        fw(r)
        left(150)
        circle(r, 180)
        left(90)
        forward(r)
        left(210)


if __name__ == '__main__':
    # draw_shape(15)
    dot(10, "red")
    draw_shape_3(200)
    # draw_shape_2(200)
    hideturtle()
    done()
