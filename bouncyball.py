import random as r
import turtle as t
from class_prog import vector


def value():
    """ this will generate my value from [-5, -3] to [3, 5] """
    return (3 + r.random() * 2) * r.choice([1, -1])


ball = vector(0, 0)
angle = 30
aim = vector(value(), value())
""" projection or movement """


def draw():
    """ move the ball and draw the screen """
    ball.move(aim)

    x = ball.x
    y = ball.y

    if x < -200 or x > 200:
        aim.x = -aim.x
    if y < -200 or y > 200:
        aim.y = -aim.y

    t.clear()
    t.goto(x, y)
    t.dot(10, "red")

    t.ontimer(draw, 50)


t.setup(420, 420, 370, 0)
t.hideturtle()
t.tracer(False)
t.up()
draw()
t.done()
