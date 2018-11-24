import random as r
import turtle as t
from class_prog import line


def draw():
    """ For drawing a maze. """
    t.color("Black")
    t.width(5)
    for x in range(-200, 200, 40):
        for y in range(-200, 200, 40):
            """ To create a matrix. """
            if r.random() > 0.5:
                line(x, y, x + 40, y + 40)
            else:
                line(x, y + 40, x + 40, y)
    t.update()


def tap(x, y):
    """ To draw line and dot in screen when you tap. """
    if abs(x) > 198 or abs(y) > 198:
        t.up()
    else:
        t.down()
    t.width(2)
    t.color("Red")
    t.goto(x, y)
    t.dot(6, "Green")


t.setup(420, 420, 370, 0)
t.hideturtle()
t.tracer(False)
draw()
t.onscreenclick(tap)
t.done()
