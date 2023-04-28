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


def draw_square(x: float, y: float, r: int, rcolor: str = "blue"):
    _goto(x - r/2, y + r/2)
    color("red")
    fillcolor(rcolor)
    pensize(2)
    begin_fill()
    for _ in range(4):
        forward(r)
        right(90)
    end_fill()


def draw_left(n: int, r: int):
    n -= 2
    if n <= 0:
        return
    _goto(-r, r/2)
    setheading(-90)

    for i in range(1, n+1):
        for _ in range(i):
            color("red")
            fillcolor("yellow")
            begin_fill()
            for _ in range(2):
                forward(r)
                right(90)
                forward(r/2)
                right(90)
            end_fill()
            forward(r)
        forward(-r*i)
        setheading(180)
        forward(r/2)
        setheading(-90)
        forward(-r/2)


def draw_right(n: int, r: int):
    n -= 2
    if n <= 0:
        return
    _goto(r, r/2)
    setheading(-90)

    for i in range(1, n+1):
        for _ in range(i):
            color("red")
            fillcolor("yellow")
            begin_fill()
            for _ in range(2):
                forward(r)
                left(90)
                forward(r/2)
                left(90)
            end_fill()
            forward(r)
        forward(-r*i)
        setheading(0)
        forward(r/2)
        setheading(-90)
        forward(-r/2)


def draw_top(n: int, r: int):
    n -= 2
    if n <= 0:
        return
    _goto(-r/2, r)
    setheading(0)

    for i in range(1, n+1):
        for _ in range(i):
            color("red")
            fillcolor("yellow")
            begin_fill()
            for _ in range(2):
                forward(r)
                left(90)
                forward(r/2)
                left(90)
            end_fill()
            forward(r)
        forward(-r*i)
        setheading(90)
        forward(r/2)
        setheading(0)
        forward(-r/2)


def draw_down(n: int, r: int):
    n -= 2
    if n <= 0:
        return
    _goto(-r/2, -r)
    setheading(0)

    for i in range(1, n+1):
        for _ in range(i):
            color("red")
            fillcolor("yellow")
            begin_fill()
            for _ in range(2):
                forward(r)
                right(90)
                forward(r/2)
                right(90)
            end_fill()
            forward(r)
        forward(-r*i)
        setheading(-90)
        forward(r/2)
        setheading(0)
        forward(-r/2)


def draw_shape(n: int, df: int):
    r = df * n
    for _ in range(n - 1):
        draw_square(0, 0, r)
        r -= df
    if n != 1:
        _goto(0, 0)
        color("red")
        for _ in range(4):
            forward(df)
            forward(-df)
            right(90)
    draw_square(0, 0, r, "yellow")
    draw_down(n, df)
    draw_left(n, df)
    draw_right(n, df)
    draw_top(n, df)


if __name__ == '__main__':
    draw_shape(4, 50)
    hideturtle()
    done()
