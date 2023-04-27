import math
from turtle import *
screensize(500, 500)


def _goto(x, y):
    hideturtle()
    penup()
    goto(x, y)
    pendown()
    showturtle()


def draw_flower_1(x: float = 0, y: float = 0, r: int = 170):
    _goto(x, y)
    setheading(90)
    left(45)
    pensize(1)
    for _ in range(5):
        color("red")
        fillcolor("red")
        begin_fill()
        for _ in range(2):
            for _ in range(90):
                forward(2*math.pi*r/1.4/360)
                right(1)
            right(90)
        end_fill()
        right(360/5)


def draw_flower_2(x: float = 0, y: float = 0, r: int = 170):
    _goto(x, y)
    color("white")
    fillcolor("white")
    penup()
    setheading(90)
    for _ in range(6):
        forward(30)
        dot(50, "white")
        forward(-30)
        right(360/6)


if __name__ == '__main__':
    r = 200
    dot((r+1)*2, "yellow")
    draw_flower_1(0, 0, r)
    draw_flower_2(0, 0, r)
    _goto(0, 0)
    dot(40, "yellow")
    hideturtle()
    done()
