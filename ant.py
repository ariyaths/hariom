
import random as r
import turtle as t
from class_prog import vector

ant = vector(0, 0)
aim = vector(2, 0)


def wrap(value):
    return value


def draw():
    ant.move(aim)
    ant.x = wrap(ant.x)
    ant.y = wrap(ant.y)
    aim.move(r.random() - 0.5)
    aim.rotate(r.random() * 10 - 5)
    t.clear()
    t.goto(ant.x, ant.y)
    t.dot(4)
    if running:
        t.ontimer(draw, 100)


t.setup(420, 420, 370, 0)
t.hideturtle()
t.tracer(False)
t.up()
running = True
draw()
t.done()
