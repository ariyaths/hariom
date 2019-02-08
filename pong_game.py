from random import choice, random
import turtle as t
from class_prog import vector


def value():
    """[-5, -3] - [3, 5]"""
    return (3 + random() * 2) * choice([1, -1])


ball = vector(0, 0)
aim = vector(value(), value())
state = {1: 0, 2: 0}


def move(player, change):
    state[player] += change


def rectangle(x, y, width, height):
    t.up()
    t.goto(x, y)
    t.down()
    t.begin_fill()
    for count in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()


def draw():
    t.clear()
    rectangle(-200, state[1], 10, 50)
    rectangle(190, state[2], 10, 50)

    ball.move(aim)
    x = ball.x
    y = ball.y
    t.dot(10, "red")
    t.update()

    if y < -200 or y > 200:
        aim.y = -aim.y

    if x < -185:
        low = state[1]
        high = state[1] + 50
        if low <= y <= high:
            aim.x = -aim.x
        else:
            return

    if x > 185:
        low = state[2]
        high = state[2] + 50
        if low <= y <= high:
            aim.x = -aim.x
        else:
            return
    t.ontimer(draw, 50)


t.setup(420, 420, 370, 0)
t.hideturtle()
t.tracer(False)
t.listen()
t.onkey(lambda: move(1, 20), "w")
t.onkey(lambda: move(1, -20), "s")
t.onkey(lambda: move(2, 20), "Up")
t.onkey(lambda: move(2, -20), "Down")
draw()
t.done()
