import math
from turtle import *
screensize(500, 500)
ang = 60


def _goto(x, y):
    hideturtle()
    penup()
    goto(x, y)
    pendown()
    showturtle()


def draw_N(x: float, y: float, r: int, n: int):
    _goto(x, y)
    setheading(ang)
    pensize(3)
    r2 = math.sqrt(2*r*r*(1-math.cos(2*math.pi / n)))
    angle1 = 360/n
    angle2 = 180 - (180 - angle1)/2
    penup()
    forward(r)
    color("blue")
    pendown()
    right(angle2)
    for _ in range(n):
        forward(r2)
        right(angle1)


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
        forward(-width)
        forward(width*2)
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
    setheading(ang)
    forward(width)
    right(90)
    right(72)
    draw_start_2(pos()[0], pos()[1], width2, False)


def draw_N_2(x: float, y: float, r: int, n: int):
    _goto(x, y)
    pensize(3)
    r2 = math.sqrt(2*r*r*(1-math.cos(2*math.pi / n)))
    angle1 = 360/n
    angle2 = 180 - (180 - angle1) / 2
    for i in range(n):
        if i % 2 == 0:
            penup()
        forward(r)
        pendown()
        right(angle2)
        forward(r2)
        forward(-r2)
        left(angle2)

        if i % 2 == 0:
            penup()
        forward(-r)
        right(angle1)


def draw_circle(x: float, y: float, r: int, rcolor: str):
    _goto(x, y)
    penup()
    setheading(-90)
    forward(r)
    setheading(0)
    pendown()
    color(rcolor)
    circle(r)


def draw_shape(x: float, y: float, r: int):
    _goto(x, y)
    r2 = r / math.sqrt(3)
    color("blue")
    for _ in range(6):
        forward(r2)
        draw_N_2(pos()[0], pos()[1], r2, 6)
        forward(-r2)
        right(360/6)

    draw_circle(x, y, r2, "yellow")
    draw_circle(x, y, r, "red")
    draw_circle(x, y, r2*2, "green")


def draw_shape_2(x: float, y: float, r: int):
    _goto(x, y)
    pensize(3)
    for _ in range(6):
        color("pink")
        circle(r)
        right(360/6)
    global ang
    ang = 90
    draw_N(0, 0, r, 3)
    ang = -90
    draw_N(0, 0, r*2, 3)


def draw_shape_3(x: float, y: float, r: int):
    _goto(x, y)
    color("blue")
    pensize(3)
    r2 = r / math.sqrt(2*(1 - math.cos(3*math.pi/5)))
    for _ in range(5):
        for _ in range(2):
            forward(r2)
            right(72)
            forward(r2)
            right(108)
        right(360/5)
    draw_circle(0, 0, r, "blue")


if __name__ == '__main__':
    # draw_N(0, 0, 100, 5)
    # draw_start_3(0, 0, 100)
    # draw_shape(0, 0, 100)
    # draw_shape_2(0, 0, 100)
    draw_shape_3(0, 0, 100)
    hideturtle()
    done()
