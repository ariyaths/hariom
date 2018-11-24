import turtle as t
from random import randrange
from class_prog import square, vector


food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
targets = []


def change(x, y):
    aim.x = x
    aim.y = y


def inside(head):
    return -200 < head.x < 200 and -200 < head.y < 200


def move():
    """ To move snake one segment forward. """
    head = snake[-1].copy()
    head.move(aim)
    if not inside(head) or head in snake:
        square(head.x, head.y, 10, "Red")
        t.update()
        return
    snake.append(head)
    if head == food:
        """ Means if snake eats food. """
        print("Snake: ", len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)
    t.clear()
    for body in snake:
        square(body.x, body.y, 10, "Black")
    square(food.x, food.y, 10, "Green")
    t.update()
    t.ontimer(move, 100)


t.setup(420, 420, 370, 0)
t.hideturtle()
t.tracer(False)
t.listen()
t.onkey(lambda: change(10, 0), "Right")
t.onkey(lambda: change(-10, 0), "Left")
t.onkey(lambda: change(0, 10), "Up")
t.onkey(lambda: change(0, -10), "Down")
move()
t.done()
