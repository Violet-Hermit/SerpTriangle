# Construction of the Serpinski triangle by the Chaos method
# Define 3 vertices of the triangle and the pointer position.
# At each step, we select 1 of 3 apexes and move pointer half the distance towards chosen apex


from random import *
from tkinter import *
import collections
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#Check whether a pointwith a simular rounded value was present earlier in the queue
def find_dif(l,elm):
    for i in range(len(l)):
        if int(l[i].x)-int(elm.x)==0 and int(l[i].y)-int(elm.y)==0:
            return False
    l.append(elm)
    return True


def prop_div(p1, p2): # return middle of segment
        return Point((p1.x+p2.x)/2, (p1.y+p2.y)/2)


def draw_point(p): # draw point
    canvas.create_line(p.x, p.y, p.x + 1, p.y, fill=colors)


#Get pointers from the queue
#Function draw all available point for this pointer
#Check whether a pointwith a simular rounded value was present earlier in the queue
#Add result to queue
def new_point(nodes, dq, l):
    point = dq.popleft()
    for i in range(len(nodes)):
        pnt = prop_div(nodes[i],point)
        if find_dif(l, pnt):
            draw_point(pnt) # draw point
            dq.append(pnt) # add new elements from queue


size = 1000 # size of screen
wnd = Tk()
canvas = Canvas(wnd, width=size, height=size)
canvas.pack()
colors = "black"
nodes = [Point(10, 10) , Point(910, 10), Point(460, 910)] # nodes of triangle
pt = Point(10,10) # pointer
dq = collections.deque()
dq.append(pt)
l = list()
while True:
    print(len(dq))
    new_point(nodes, dq, l)
    wnd.update() # update