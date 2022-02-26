# Construction of the Serpinski triangle by the Chaos method
# Define 3 vertices of the triangle and the pointer position.
# At each step, we select 1 of 3 apexes and move pointer half the distance towards chosen apex

from random import *
from tkinter import *


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
def prop_div(p1, p2): # segment line middle point selection
    return (p1.x+p2.x)/2, (p1.y+p2.y)/2


size = 1000 # size of screen
wnd = Tk()
canvas = Canvas(wnd, width=size, height=size)
canvas.pack()
colors = "black"
nodes = [Point(10, 10) , Point(910, 10), Point(460, 910)] # nodes of triangle
pt = Point(10,10) # pointer
while True:
    ver =  choice(nodes) # select random node
    pt.x, pt.y = prop_div(pt, ver) # pointer position change
    canvas.create_line(pt.x, pt.y, pt.x+1, pt.y, fill=colors)# draw "point"
    wnd.update()# update