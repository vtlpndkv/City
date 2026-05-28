from turtle import *
from random import *
pensize(3)
speed(0)

def priroda():
    penup()
    goto(-300, 25)
    color('blue')
    pendown()
    begin_fill()
    for i in range(2):
        forward(600)
        left(90)
        forward(300)
        left(90)
    end_fill()

    for i in range(100):
        z1 = randint(-300, 300)
        z2 = randint(-300, 300)
        penup()
        goto(z1, z2)
        dot(3, 'white')
        pendown()

    penup()
    goto(150, 200)
    color('white')
    begin_fill()
    circle(20)
    penup()
    end_fill()

    penup()
    goto(-300, -100)
    color('#009900')
    pendown()
    begin_fill()
    for i in range(2):
        forward(600)
        left(90)
        forward(150)
        left(90)
    end_fill()

def make_window(x, y):
    penup()
    goto(x, y)
    pendown()
    light = randint(0, 3)
    if light == 1:
        color('yellow')
    elif light == 2:
        color('orange')
    elif light == 3:
        color('purple')
    else:
        color('blue')
    begin_fill()
    for i in range(4):
        forward(15)
        left(90)
    end_fill()
    color('black')
    for i in range(4):
        forward(15)
        left(90)
    forward(7.5)
    left(90)
    forward(15)
    right(90)
    forward(7.5)
    x += 20

    penup()
    goto(x, y)
    pendown()
    light = randint(0, 3)
    if light == 1:
        color('yellow')
    elif light == 2:
        color('orange')
    elif light == 3:
        color('purple')
    else:
        color('blue')
    begin_fill()
    for i in range(4):
        forward(15)
        left(90)
    end_fill()
    color('black')
    for i in range(4):
        forward(15)
        left(90)
    forward(7.5)
    left(90)
    forward(15)
    right(90)
    forward(7.5)

def make_build(count):
    for i in range(count):
        x = randint(-250, 250)
        y = randint(-100, 10)
        penup()
        goto(x, y)
        color('gray')
        pendown()
        begin_fill()
        for i in range(2):
            forward(50)
            left(90)
            forward(110)
            left(90)
        end_fill()
        color('black')
        for i in range(2):
            forward(50)
            left(90)
            forward(110)
            left(90)
        x += 7.5
        y += 30
        make_window(x, y)
        y += 20
        make_window(x, y)
        y += 20
        make_window(x, y)



priroda()
c = int(input("Введите кол-во зданий: "))
make_build(c)
hideturtle()
exitonclick()