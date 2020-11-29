# -*- coding: utf-8 -*-

from calysto.graphics import *
from calysto.display import display, clear_output

#image_width=512
image_width=0
canvas=None
color=None
rect=None

#初期化
def init(size, r, g, b):
    global image_width
    global canvas
    global color
    global rect
    image_width=size
    canvas=Canvas(size=(image_width, image_width))
    color=Color(r, g, b)
    rect=Rectangle(size=(image_width, image_width), fill=color, stroke=color)
    #rect.fill(color)

# 線分を書く
def draw_line(p1_x, p1_y, p2_x, p2_y):
    def conv(z):
        return (image_width * z)
    start=(conv(p1_x), image_width - conv(p1_y))
    end=(conv(p2_x), image_width - conv(p2_y))
    line=Line(start, end)
    #line.extras["stroke"]=color
    canvas.draw(line)

# キャンバスのクリア
def clear():
    canvas.clear()
    canvas.draw(rect)

# キャンバスへの反映
def update():
    display(canvas)
