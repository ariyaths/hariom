# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 13:18:00 2020

@author: HariOm12
"""

import turtle as tl

state = {'turn': 0}

def spinner():
    "Draw fidget spinner."
    tl.clear()
    angle = state['turn'] / 10
    tl.right(angle)
    tl.forward(100)
    tl.dot(120, 'red')
    tl.back(100)
    tl.right(120)
    tl.forward(100)
    tl.dot(120, 'green')
    tl.back(100)
    tl.right(120)
    tl.forward(100)
    tl.dot(120, 'blue')
    tl.back(100)
    tl.right(120)
    tl.update()

def animate():
    "Animate fidget spinner."
    if state['turn'] > 0:
        state['turn'] -= 1

    spinner()
    tl.ontimer(animate, 20)

def flick():
    "Flick fidget spinner."
    state['turn'] += 10

tl.setup(420, 420, 370, 0)
tl.hideturtle()
tl.tracer(False)
tl.width(20)
tl.onkey(flick, 'space')
tl.listen()
animate()
tl.done()
tl.bye()

print("hi")