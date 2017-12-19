from math import *
from random import *
from turtle import *

def tree(branchLen):
    old_color = color()
    old_width = width()
    if branchLen >= 20:
        color("brown")
        width(branchLen / 5.0)
    elif branchLen >= 10:
        color((0.0, random() / 2.0 + 0.5, 0.0))
        width(5)
    else:
        return
    forward(branchLen)
    right(60)
    for i in range(4):
        tree(int(branchLen / 1.5))
        left(40)
    right(100)
    backward(branchLen)
    width(old_width)
    color(*old_color)

speed(0)
left(90)
tree(80)
done()