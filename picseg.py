# -*- coding: utf-8 -*-

from calysto.graphics import *
from calysto.display import display, clear_output

#image_width=512
image_width=256
canvas=Canvas(size=(image_width, image_width))
color=Color(255, 0, 0)

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

# キャンバスへの反映
def update():
    display(canvas)
