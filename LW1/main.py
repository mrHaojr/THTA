import math
from turtle import *
screensize(500, 500)


def _goto(x, y):
    hideturtle()
    penup()
    goto(x, y)
    pendown()
    showturtle()


def draw_rectangle(x: float, y: float, width: int, height: int, color, filled=False):
    _goto(x, y)
    # if filled rectangle
    if filled:
        fillcolor(color)
        begin_fill()
    # main
    for _ in range(2):
        forward(width)
        right(90)
        forward(height)
        right(90)
    # if filled rectangle
    if filled:
        end_fill()


def draw_tree(x, y, l):
    _goto(x, y)
    setheading(90)
    color("white")
    pensize(3)
    for _ in range(6):
        forward(l)
        for _ in range(8):
            forward(10)
            forward(-10)
            rt(360/8)
        forward(-l)
        rt(360/6)


def _veHinhBongTuyet(width: int, height: int):
    draw_rectangle(-width//2, height//2, width, height, "red", True)
    draw_tree(0, 0, 150)


def draw_start(x: float, y: float, width: int):
    color("black")
    _goto(x, y)
    fillcolor("yellow")
    begin_fill()
    for _ in range(5):
        forward(width)
        right(144)
    end_fill()


def draw_start_2(x: float, y: float, width: int, filled: bool = False):
    '''
    draw start in (x, y) with width and filled true if filled shape or none

    '''
    color("red")
    _goto(x, y)
    pensize(2)
    if filled:
        fillcolor("yellow")
        begin_fill()

    for _ in range(5):
        forward(width)
        left(72)
        forward(width)
        right(144)

    if filled:
        end_fill()


def draw_start_3(x: float, y: float, width: int):
    '''
    draw star main point (x, y) with width is from main point to canh
    '''
    _goto(x, y)
    width2 = width * math.sqrt((1-math.cos(2*math.pi/5)) /
                               (1-math.cos(3*math.pi/5)))
    penup()
    setheading(90)
    forward(width)
    setheading(0)
    right(72)
    draw_start_2(pos()[0], pos()[1], width2, True)


'''
if filled:
        fillcolor("yellow")
        begin_fill()

    for _ in range(5):
        forward(width)
        right(162)
        forward(width2)
        forward(-width2)
        right(-162*2)
        forward(width2)
        forward(-width2)
        right(162)
        forward(-width)
        right(72)

    if filled:
        end_fill()
'''


def _veHinhDenOngSao(x: float, y: float, r: float):
    color("black")
    _goto(x, y)
    setheading(-90)
    pensize(12)
    forward(250)
    _goto(x, y)
    dot(r*2 + 2, "red")
    draw_start_3(x, y, r)


if __name__ == '__main__':
    hideturtle()
    # _veHinhBongTuyet(600, 400)
    _veHinhDenOngSao(0, 0, 100)
    hideturtle()
    done()
