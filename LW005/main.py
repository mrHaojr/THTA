from turtle import *
screensize(500, 500)


def _goto(x, y):
    hideturtle()
    penup()
    goto(x, y)
    pendown()
    showturtle()


def draw_one(x: float, y: float, r: int, width: int):
    _goto(x, y)
    pensize(2)
    forward(r)
    left(45)
    for _ in range(4):
        forward(width)
        right(90)
    right(45)
    forward(-r)


def draw_all(x: float, y: float, r: int, width: int):
    _goto(x, y)
    n = 25
    for _ in range(n):
        draw_one(x, y, r, width)
        right(360/n)


if __name__ == '__main__':
    draw_all(0, 0, 100, 20)
    hideturtle()
    done()
