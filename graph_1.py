from turtle import *

def star():
    color('red', 'yellow')
    begin_fill()
    while True:
        forward(200)
        left(170)
        if abs(pos()) < 1:
            break
    end_fill()


def triunghi(size):
    forward(size)
    left(120)
    forward(size)
    left(120)
    forward(100)
    left(120)

def triunghi2(size):
    for i in range(3):
        forward(size)
        left(120)
    
def patrat2(size):
    for i in range(4):
        forward(size)
        left(90)

def hexagon2(size):
    for i in range(6):
        forward(size)
        left(60)

def poligon(size=10, n=3):
    for i in range(n):
        forward(size)
        left(360/n)

def Cword(size):
    left(90)
    forward(size/2)
    right(90)
    forward(size)
    right(90)
    forward(size/10)
    right(90)
    forward(9*size/10)
    left(90)
    forward(size - 20)
    left(90)
    forward(9*size/10)
    right(90)
    forward(size/10)
    right(90)
    forward(size)
    right(90)
    forward(size/2)
    right(90)

def multipleC():
    m = 12
    for j in range(m):
        Cword(100)
        right(360/m)

def circle2(radius):
    for i in range(50):
        forward(radius)
        left(360/50)

def circlepattern(nr,radius1, radius2):
    for k in range(nr):
        forward(radius1)
        circle2(radius2)
        left(180)
        forward(radius1)
        left(360-360/nr)

# Set the colors for drawing
colors = ['violet', 'indigo', 'blue', 
       'green', 'yellow', 'orange', 'red']
def circlepatter2(nr, radius1, radius2):
    for k in range(nr):
        penup()
        forward(radius1)
        pendown()
        color(colors[k % 7])
        circle(radius2)
        penup()
        forward(-radius1)
        left(360/nr)


circlepatter2(16,50,20)  

done()