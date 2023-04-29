import math
import random
from turtle import *
screensize(800, 500)


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


def draw_n(n: int, base: int, df: int, ang: int = 60):
    pensize(2)
    if n == 0:
        color("green")
        forward(base)
        forward(-base)
        color("black")
        return
    forward(base)
    right(ang/2)
    draw_n(n - 1, base - df, df, ang)
    left(ang)
    draw_n(n - 1, base - df, df, ang)
    right(ang/2)
    forward(-base)


def draw_cay_de_quy():
    setheading(90)
    _goto(0, -300)
    base = 9
    n = 7
    draw_n(n, base*(n+1), base, 60)


def draw_circle(r: int):
    fw(-r)
    right(90)
    circle(r)
    left(90)
    fw(r)


def draw_square(r: int, n: int):
    for _ in range(4):
        for _ in range(2):
            for _ in range(4):
                for _ in range(n - 1):
                    draw_circle(r)
                    fw(r*2)
                left(90)
            fw(r*2*n)
        fw(r*2*n - r*2)
        left(90)


def draw_shape(r: int, n: int):
    color("blue")
    pensize(2)
    setheading(0)
    hv = n*6*r
    _goto(- hv/2 + r, - hv/2 + r)
    draw_square(r, n)


def draw_one2(r: int):
    dot(2*r, rand_color(1000))
    d = 6*r
    fw(-d/2)
    right(90)
    fw(d/2)
    left(90)
    color("blue")
    for _ in range(4):
        forward(d)
        left(90)
    right(90)
    fw(-d/2)
    left(90)
    fw(d/2)


def draw_two(r: int):
    dot(2*r, rand_color(1000))
    for _ in range(2):
        fw(2*r)
        left(90)
    for _ in range(4):
        for _ in range(2):
            draw_one2(r/3)
            fw(2*r)
        left(90)
    for _ in range(2):
        right(90)
        fw(-2*r)


def draw_vien_tron_de_quy(n: int, r: int):
    if n == 1:
        draw_one2(r)
        return
    dot(2*r, rand_color(1000))
    for _ in range(2):
        fw(2*r)
        left(90)
    for _ in range(4):
        for _ in range(2):
            draw_vien_tron_de_quy(n - 1, r/3)
            fw(2*r)
        left(90)
    for _ in range(2):
        right(90)
        fw(-2*r)


if __name__ == '__main__':
    # draw_cay_de_quy()
    # dot(10, "red")
    # draw_shape(10, 3)
    # draw_two(90)
    draw_vien_tron_de_quy(4, 90)
    # hideturtle()
    done()
