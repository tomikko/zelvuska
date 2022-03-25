import turtle
import random
t = turtle.Turtle()
screen = turtle.getscreen()
t.speed(30)

sirka = 30
vyska = 100
def kniha(sirka,vyska):
    for i in range(2):
        t.fd(sirka)
        t.lt(90)
        t.fd(vyska)
        t.lt(90)

def shelf():
    for i in range(2):
        t.fd(400)
        t.lt(90)
        t.fd(100)
        t.lt(90)

def line():
    t.fd(600)

t.pu()
t.goto(-200, -300)
t.lt(90)
t.pd()
line()
t.pu()
t.goto(200, -300)
t.pd()
line()
t.pu()
t.goto(-200, -200)
t.pd()

for i in range(4):
    t.rt(90)
    shelf()
    t.lt(90)
    t.fd(100)

min_width = 20
max_width = 30
min_height = 60
max_height = 80


def book():
    width = random.randint(min_width, max_width)
    height = random.randint(min_height, max_height)
    for i in range(2):
        t.fd(width)
        t.lt(90)
        t.fd(height)
        t.lt(90)

    t.fd(width)

t.rt(90)
t.fd(10)
t.speed(0)

t.screen.colormode(255)
def color():
    R = random.randint(0, 255)
    B = random.randint(0, 255)
    G = random.randint(0, 255)

    turtle.fillcolor(R, G, B)

for i in range(10):
    t.begin_fill()
    color()
    book()
    t.end_fill()