from turtle import *
import math
screensize(500, 500)


def _goto(x, y):
    hideturtle()
    penup()
    goto(x, y)
    pendown()
    showturtle()


def _ria(x, y, width):
    _goto(x - width, y + width)
    pensize(5)
    color("blue")
    setheading(0)
    for _ in range(4):
        for _ in range(90):
            forward(width / 4)
            forward(-width / 4)
            right(1)
        right(-90)
        forward(width*2)
        right(90)


def draw_flower_1(rcolor: str, x: float = 0, y: float = 0, r: int = 170):
    _goto(x, y)
    setheading(90)
    left(45)
    pensize(1)
    for _ in range(6):
        color(rcolor)
        fillcolor(rcolor)
        begin_fill()
        for _ in range(2):
            for _ in range(90):
                forward(2*math.pi*r/1.4/360)
                right(1)
            right(90)
        end_fill()
        right(360/6)


if __name__ == '__main__':
    width = 120
    _ria(0, 0, width)
    draw_flower_1("red", 0, 0, width * 2 / 3)
    draw_flower_1("blue", 0, 0, width * 1 / 3)
    hideturtle()
    done()
