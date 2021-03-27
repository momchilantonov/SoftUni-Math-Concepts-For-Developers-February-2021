from turtle import *


def koch_curve(length_side, levels):
    if levels == 0:
        forward(length_side)
        return
    length_side /= 3
    koch_curve(length_side, levels - 1)
    left(60)
    koch_curve(length_side, levels - 1)
    right(120)
    koch_curve(length_side, levels - 1)
    left(60)
    koch_curve(length_side, levels - 1)


def draw_snowflake(length_side, levels):
    # pen(fillcolor="violet", pencolor="magenta")
    # pen(fillcolor="blue", pencolor="violet")
    # pen(fillcolor="#62C6F0", pencolor="#0029D5")
    pen(fillcolor="#62C6F0", pencolor="#FF5DF7")
    begin_fill()
    speed("fastest")
    up()
    backward(length_side / 2)
    down()
    for _ in range(3):
        koch_curve(length_side, levels)
        right(120)
    end_fill()
    done()


draw_snowflake(300, 4)

# # main function
# if __name__ == "__main__":
#     # defining the speed of the turtle
#     speed(0)
#     length = 300.0
#
#     # Pull the pen up – no drawing when moving.
#     penup()
#
#     # Move the turtle backward by distance,
#     # opposite to the direction the turtle
#     # is headed.
#     # Do not change the turtle’s heading.
#     backward(length / 2.0)
#
#     # Pull the pen down – drawing when moving.
#     pendown()
#
#     snowflake(length, 4)
#
#     # To control the closing windows of the turtle
#     mainloop()
