from tkinter import *
from math import *
 
root = Tk()
c = Canvas(root, width=600, height=600, bg="white")
c.create_oval(100, 100, 500, 500, outline='black')
c.pack()
 
ball = c.create_oval(0, 100, 40, 140, fill='green')

speed = 10
direction = True
angle = 0
 
def motion():
    global speed, direction, angle
    if angle >= 360:
        angle = 0
    if direction:
        x = cos(radians(angle))*200
        y = sin(radians(angle))*200
    else:
        y = cos(radians(angle))*200
        x = sin(radians(angle))*200
    angle += 1
    c.coords(ball, 295 + x, 295 + y, 305 + x, 305 + y)
    root.after(speed, motion)
 
motion()
root.mainloop()
