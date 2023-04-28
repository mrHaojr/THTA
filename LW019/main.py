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


def draw_triagle(n: int):
    color("blue")
    begin_fill()
    for _ in range(3):
        forward(n)
        left(360/3)
    end_fill()


def draw_dq(base: int, n: int):
    if n == 0:
        draw_triagle(base)
        return

    for _ in range(3):
        draw_dq(base, n - 1)
        forward(base*2**n)
        left(360/3)


def draw_shape(r: int):
    _goto(0, 0)
    dot(r*4, "black")
    pensize(2)
    setheading(0)
    dot(4, "white")
    for _ in range(4):
        fw(r)
        dot((r-1)*2, "white")
        fw(-r)
        right(90)
    fw(2*r)
    right(135)
    begin_fill()
    for _ in range(4):
        forward(2*math.sqrt(2*r**2))
        right(90)
    end_fill()
    left(135)
    fw(-2*r)
    dot(2*math.sqrt(2*r**2), "white")
    for _ in range(4):
        right(90)
        circle(r)
        left(90)
        right(90)
    fw(r)
    right(90)
    fw(r)
    right(90)
    for _ in range(4):
        forward(2*r)
        right(90)


def draw_shape_3(d: int):
    _goto(0, 0)
    setheading(0)
    pensize(2)
    for _ in range(4):
        color("black")
        fillcolor("blue")
        # hcn phan tu
        begin_fill()
        for _ in range(4):
            forward(d)
            left(90)
        end_fill()
        # ------------
        # 1/4 hinh tron trang
        fillcolor("white")
        begin_fill()
        forward(d)
        left(90)
        circle(d, 90)
        left(90)
        forward(d)
        end_fill()
        left(90)
        # -------------------
        # hinh tron nho xa
        fillcolor("blue")
        begin_fill()
        forward(d)
        left(90)
        circle(d/4, 180)
        right(90)
        forward(-d/2)
        end_fill()
        forward(d)
        right(180)
        # -------
        fillcolor("blue")
        begin_fill()
        circle(d/2, 180)
        left(90)
        forward(d)
        end_fill()
        # ---------
        fillcolor("white")
        begin_fill()
        left(90)
        circle(d/4, 180)
        left(90)
        forward(d/2)
        end_fill()


if __name__ == '__main__':
    draw_shape_3(200)
    # base = 20
    # n = 5
    # dot(10, "red")
    # _goto(-base*n*2, -300)
    # draw_dq(base, n)
    # draw_shape(100)
    # hideturtle()
    done()
