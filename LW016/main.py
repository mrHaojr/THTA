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


def draw_shape(d: int):
    _goto(0, 0)
    r2 = d*math.sqrt(3)/3
    r3 = d*math.sqrt(3)/6
    color("black")
    dot((r3+d+1)*2, "green")
    # draw three circle
    setheading(180)
    for _ in range(3):
        penup()
        forward(r3 + d/2)
        pendown()
        right(90)
        dot(d, "white")
        left(90)
        penup()
        forward(-r3 - d/2)
        pendown()
        right(360/3)
    _goto(0, 0)
    setheading(90)
    left(30)
    penup()
    forward(r2)
    pendown()
    right(150)
    color("black")
    fillcolor("brown")
    begin_fill()
    for _ in range(3):
        forward(d)
        right(360/3)
    end_fill()


def draw_shape_2(d: int):
    _goto(0, 0)
    d1 = d / math.cos(math.pi/8)
    r = d1*math.sqrt(2*(1-math.cos(math.pi/4)))
    setheading(90)
    pensize(2)
    for _ in range(8):
        penup()
        forward(d)
        left(90)
        forward(r/2)
        pendown()
        rcolor = rand_color(1000)
        color(rcolor)
        fillcolor(rcolor)
        begin_fill()
        for _ in range(4):
            right(90)
            forward(r)
        end_fill()
        penup()
        forward(-r/2)
        right(90)
        forward(-d)
        pendown()
        right(360/8)


if __name__ == '__main__':
    draw_shape_2(100)
    # draw_shape(120)
    hideturtle()
    done()
