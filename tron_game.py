import turtle as t
from class_prog import square, vector

""" For player 1. """
player1xy = vector(-300, 0)
player1aim = vector(4, 0)
player1body = set()
""" For player 2. """
player2xy = vector(300, 0)
player2aim = vector(-4, 0)
player2body = set()


def inside(head):
    """ Return true if head inside boundary. """
    return -400 < head.x < 400 and -400 < head.y < 400


def draw():
    player1xy.move(player1aim)
    player1head = player1xy.copy()

    player2xy.move(player2aim)
    player2head = player2xy.copy()

    """ SUJIT: I added missing Line 74 in class_prog [return self._hash] """
    if not inside(player1head) or (player1head in player2body):
        print("The blue player has won")
        return
    if not inside(player2head) or (player2head in player1body):
        print("The red player has won")
        return

    player1body.add(player1head)
    player2body.add(player2head)
    square(player1xy.x, player1xy.y, 3, "Red")
    square(player2xy.x, player2xy.y, 3, "Blue")
    t.update()
    t.ontimer(draw, 50)


t.setup(820, 820, 370, 0)
t.hideturtle()
t.tracer(False)
t.listen()
t.onkey(lambda: player1aim.rotate(90), "a")
t.onkey(lambda: player1aim.rotate(-90), "d")
t.onkey(lambda: player2aim.rotate(90), "j")
t.onkey(lambda: player2aim.rotate(-90), "l")
draw()
t.done()
