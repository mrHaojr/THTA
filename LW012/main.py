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


def draw_triagle(n: int, r: int):
    r2 = r*math.sqrt(2)/2
    if n % 2 != 0:
        begin_fill()
        right(45)
        forward(r2)
        right(90)
        forward(r2)
        right(135)
        forward(r)
        end_fill()
        right(90)

        forward(r)
        begin_fill()
        right(135)
        forward(r2)
        left(90)
        forward(r2)
        left(135)
        forward(r)
        end_fill()
        right(90)
        forward(-r)
    else:
        begin_fill()
        right(45)
        forward(r2)
        left(90)
        forward(r2)
        left(135)
        forward(r)
        end_fill()

        setheading(-90)
        forward(r)
        begin_fill()
        left(135)
        forward(r2)
        right(90)
        forward(r2)
        right(135)
        forward(r)
        end_fill()
        setheading(90)
        forward(r)
        setheading(0)


def draw_shape_1(n: int):
    r = 50
    _goto(0 - r/2, 250)
    color("blue")
    pensize(2)
    for i in range(1, n + 1):
        for _ in range(i):
            for _ in range(4):
                forward(r)
                right(90)
            draw_triagle(i, r)
            forward(r)
        if (i != n):
            forward(-r*i)
            setheading(-90)
            forward(r)
            setheading(0)
            forward(-r/2)


def draw_square(x: float, y: float, r: int):
    color("blue")
    _goto(x, y)
    begin_fill()
    for _ in range(4):
        forward(r)
        right(90)
    end_fill()


def draw_V(r: int, x: float, y: float):
    setheading(0)
    color("blue")
    pensize(1)
    _goto(x - 3*r/2, y + 3*r/2)
    for _ in range(4):
        forward(r*3)
        right(90)

    draw_square(x - r/2, y+r/2, r)
    draw_square(x - 3*r/2, y+3*r/2, r)
    draw_square(x + r/2, y+3*r/2, r)
    draw_square(x - 3*r/2, y-r/2, r)
    draw_square(x + r/2, y-r/2, r)


def draw_shape_2(n: int):
    r = 30
    setheading(0)
    draw_V(r, 0, 0)
    x, y = 0, 0
    for _ in range(1, n):
        x += 2*r
        y += 2*r
        draw_V(r, x, y)

    x, y = 0, 0
    for _ in range(1, n):
        x -= 2*r
        y += 2*r
        draw_V(r, x, y)

    x, y = 0, 0
    for _ in range(1, n):
        x += 2*r
        y -= 2*r
        draw_V(r, x, y)

    x, y = 0, 0
    for _ in range(1, n):
        x -= 2*r
        y -= 2*r
        draw_V(r, x, y)


if __name__ == '__main__':
    # draw_shape_1(10)
    draw_shape_2(3)
    hideturtle()
    done()
