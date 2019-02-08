import random as r
import turtle as t
from class_prog import vector


bird = vector(0, 0)
balls = []


def inside(point):
    """ To return true if point on screen. """
    return -200 < point.x < 200 and -200 < point.y < 200


def tap(x, y):
    """ To move our bird in response. """
    up = vector(0, 50)
    if -1000 < x < 1000 and -1000 < y < 1000:
        bird.move(up)


def draw(alive):
    """ To draw screen objects. """
    """ Alive is boolean. """
    t.clear()
    t.goto(bird.x, bird.y)
    if alive:
        t.dot(10, "green")
    else:
        t.dot(10, "red")
    for ball in balls:
        t.goto(ball.x, ball.y)
        t.dot(20, "black")
    t.update()


def move():
    """ To update object position. """
    bird.y -= 1

    for ball in balls:
        ball.x -= 1

    if r.randrange(10) == 0:
        y = r.randrange(-199, 199)
        ball = vector(199, y)
        balls.append(ball)

    while len(balls) > 0 and not inside(balls[0]):
        balls.pop(0)

    if not inside(bird):
        draw(False)
        return

    for ball in balls:
        if abs(ball - bird) < 15:
            draw(False)
            return

    draw(True)
    t.ontimer(move, 50)


t.setup(420, 420, 370, 0)
t.hideturtle()
t.up()
t.tracer(False)
t.onscreenclick(tap)
move()
t.done()
