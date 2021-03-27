from turtle import *


def sierpinski(length_side, level):
    if level == 0:
        for _ in range(3):
            forward(length_side)
            left(120)
    else:
        sierpinski(length_side / 2, level - 1)
        forward(length_side / 2)
        sierpinski(length_side / 2, level - 1)
        backward(length_side / 2)
        left(60)
        forward(length_side / 2)
        right(60)
        sierpinski(length_side / 2, level - 1)
        left(60)
        backward(length_side / 2)
        right(60)


def draw_sierpinski_triangle(length_side, level):
    pen(fillcolor="#41FE3A", pencolor="#FF5733", pensize=2)
    begin_fill()
    speed("fastest")
    up()
    backward(length_side / 2)
    down()
    sierpinski(length_side, level)
    end_fill()
    done()


draw_sierpinski_triangle(300, 4)
