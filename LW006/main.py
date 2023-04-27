import math
from turtle import *
screensize(500, 500)


def _goto(x, y):
    hideturtle()
    penup()
    goto(x, y)
    pendown()
    showturtle()


def draw_N(x: float, y: float, r: int, n: int):
    _goto(x, y)
    setheading(90)
    pensize(3)
    r2 = math.sqrt(2*r*r*(1-math.cos(2*math.pi / n)))
    angle1 = 360/n
    angle2 = 180 - (180 - angle1) / 2
    for _ in range(n):
        forward(r)
        right(angle2)
        forward(r2)
        forward(-r2)
        left(angle2)

        forward(-r)
        right(angle1)


def draw_N_color(x: float, y: float, r: int, n: int, color: str = "red"):
    _goto(x, y)
    setheading(90)
    pensize(3)
    r2 = math.sqrt(2*r*r*(1-math.cos(2*math.pi / n)))
    angle1 = 360/n
    angle2 = 180 - (180 - angle1)/2
    penup()
    forward(r)
    pendown()
    fillcolor(color)
    right(angle2)
    begin_fill()
    for _ in range(n):
        forward(r2)
        right(angle1)
    end_fill()


if __name__ == '__main__':
    draw_N_color(0, 0, 100, 5)
    hideturtle()
    done()
