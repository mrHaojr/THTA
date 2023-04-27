from turtle import *
screensize(500, 500)


def _goto(x, y):
    hideturtle()
    penup()
    goto(x, y)
    pendown()
    showturtle()


def draw_square(x: float = 0, y: float = 0, r: int = 200):
    _goto(x - r//2, y + r // 2)
    color("pink")
    pensize(2)
    for _ in range(4):
        forward(r)
        right(90)


def draw_cr2(x: float = 0, y: float = 0, r: int = 100, rcolor="pink"):
    _goto(x, y)
    color(rcolor)
    fillcolor(rcolor)
    begin_fill()
    pensize(0)
    forward(r)
    left(90)
    circle(r, 90)
    left(90)
    forward(r)
    end_fill()


def draw_circle(x: float = 0, y: float = 0, r: int = 100):
    draw_cr2(x, y, r, "pink")
    draw_cr2(x, y, r, "green")
    draw_cr2(x, y, r, "blue")
    draw_cr2(x, y, r, "orange")
    _goto(x, y)
    dot(r, "white")


if __name__ == '__main__':
    draw_square(0, 0, 200)
    draw_circle(0, 0, 100)
    hideturtle()
    done()
