
import random as r
import turtle as t
from class_prog import vector, floor


tiles = {}
neighbors = [
    vector(100, 0),
    vector(-100, 0),
    vector(0, 100),
    vector(0, -100)
]


def load():
    count = 1
    for y in range(-200, 200, 100):
        for x in range(-200, 200, 100):
            mark = vector(x, y)
            tiles[mark] = count
            count += 1

    tiles[mark] = None
    for count in range(1000):
        neighbor = r.choice(neighbors)
        spot = mark + neighbor

        if spot in tiles:
            number = tiles[spot]
            tiles[spot] = None
            tiles[mark] = number
            mark = spot


def square(mark, number):
    t.up()
    t.goto(mark.x, mark.y)
    t.down()
    t.color("black", "white")
    t.begin_fill()
    for count in range(4):
        t.forward(99)
        t.left(90)
    t.end_fill()

    if number is None:
        return
    elif number < 10:
        t.forward(20)
        """ To get the number in spot. """
    t.write(number, font=("Marvel", 60, "normal"))


def tap(x, y):
    """ To swap the tiles. """
    x = floor(x, 100)
    y = floor(y, 100)
    mark = vector(x, y)

    for neighbor in neighbors:
        spot = mark + neighbor
        if spot in tiles and tiles[spot] is None:
            number = tiles[mark]
            tiles[spot] = number
            square(spot, number)
            tiles[mark] = None
            square(mark, None)


def draw():
    """ To draw all tiles. """
    for mark in tiles:
        square(mark, tiles[mark])
        t.update()


t.setup(420, 420, 370, 0)
t.hideturtle()
t.tracer(False)
load()
draw()
t.onscreenclick(tap)
t.done()
