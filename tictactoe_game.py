import turtle as t
from class_prog import line


def grid():
    """ For tic tac toe grid. """
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def draw_x(x, y):
    """ To draw X player. """
    line(x, y, x + 13, y + 13)
    line(x, y + 133, x + 133, y)


def draw_o(x, y):
    """ To draw round or circle player. """
    t.up()
    t.goto(x + 67, y + 5)
    t.down()
    t.circle(62)


def floor(value):
    return ((value + 200) // 133) * 133 - 200


def tap(x, y):
    """ To draw X or O on tapped surface. """
    x = floor(x)
    y = floor(y)
    player = state["player"]
    draw = players[player]
    state["player"] = not player


state = {"player": 0}
players = [draw_x, draw_o]


t.setup()
t.hideturtle()
t.tracer(False)
grid()
t.update()
t.onscreenclick(tap)
t.done()
