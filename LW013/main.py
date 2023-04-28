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


def draw_square(r: int):
    color("red")
    pensize(2)
    fillcolor("blue")
    begin_fill()
    for _ in range(4):
        forward(r)
        right(90)
    end_fill()


def draw_vien(r: int):
    color("red")
    pensize(2)
    for _ in range(4):
        forward(r)
        right(90)


def draw_1(r: int):
    draw_square(r)
    x, y = pos()[0], pos()[1]
    _goto(x + r/2, y)
    pendown()
    color("green")
    begin_fill()
    forward(r/2)
    right(90)
    forward(r/2)
    right(135)
    forward(r*math.sqrt(2)/2)
    end_fill()

    _goto(x, y - r/2)
    setheading(-90)
    begin_fill()
    forward(r/2)
    left(90)
    forward(r/2)
    left(135)
    forward(r*math.sqrt(2)/2)
    end_fill()
    _goto(x, y)
    setheading(0)
    draw_vien(r)


def draw_2(r: int):
    draw_square(r)
    x, y = pos()[0], pos()[1]
    pendown()
    color("green")
    begin_fill()
    forward(r/2)
    right(135)
    forward(r*math.sqrt(2)/2)
    right(135)
    forward(r / 2)
    end_fill()

    _goto(x + r/2, y - r)
    setheading(0)
    begin_fill()
    forward(r/2)
    left(90)
    forward(r/2)
    left(135)
    forward(r*math.sqrt(2)/2)
    end_fill()
    _goto(x, y)
    setheading(0)
    draw_vien(r)


def draw_shape(n: int, m: int, r: int):
    _goto(-320, 300)
    n *= 2
    m *= 2
    for i in range(n):
        for j in range(m):
            if i % 2 == 0:
                if j % 2 == 0:
                    draw_1(r)
                else:
                    draw_2(r)
            else:
                if j % 2 == 0:
                    draw_2(r)
                else:
                    draw_1(r)
            penup()
            forward(r)
            pendown()
        penup()
        forward(-r*m)
        setheading(-90)
        forward(r)
        setheading(0)
        pendown()


if __name__ == '__main__':
    draw_shape(1, 2, 40)
    hideturtle()
    done()
