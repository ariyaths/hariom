import random as r
import turtle as t
from class_prog import vector


ball = vector(-200, -200)
speed = vector(0, 0)
targets = []


def inside(xy):
    return -200 < xy.x < 200 and -200 < xy.y < 200


def tap(x, y):
    """ Will respond to the screen. """
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25


def draw():
    """ Draw the ball and targets. """
    t.clear()
    for target in targets:
        t.goto(target.x, target.y)
        t.dot(20, "blue")
    if inside(ball):
        t.goto(ball.x, ball.y)
        t.dot(10, "red")
    t.update()


def move():
    """ For movement of ball and target. """
    if r.randrange(40) == 0:
        y = r.randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)
    for target in targets:
        target.x -= 0.5
    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)
    dupe = targets.copy()
    """ Dupe is duplicate. """
    targets.clear()
    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)
    draw()
    for target in targets:
        if not inside(target):
            return
    t.ontimer(move, 50)


t.setup(420, 420, 370, 0)
t.hideturtle()
t.up()
t.tracer(False)
t.onscreenclick(tap)
move()
t.done()
