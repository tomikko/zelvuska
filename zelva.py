import turtle
import random
triangle = turtle.Turtle()
triangle.shape("triangle")
triangle.pen(pencolor = "brown", fillcolor = "brown")
triangle.lt(90)
triangle.pu()
triangle.goto(-300, -300)
circle = triangle.clone()
circle.shape("circle")
circle.pen(pencolor = "green", fillcolor = "green")
circle.pu()
circle.goto(300, -300)
triangle.goto(-300, 200)

triangle.pd()
triangle.rt(90)
triangle.fd(25)
for i in 1,2:
    triangle.lt(120)
    triangle.fd(50)
triangle.lt(120)
triangle.fd(25)
triangle.pu()

triangle.lt(90)
triangle.goto(-300, -300)
circle.goto(300, 225)
circle.pd()
circle.circle(25)
circle.pu()
circle.lt(90)
circle.fd(25)
circle.rt(90)
circle.goto(275, -300)
print("Begin!")
die = [1,2,3,4,5,6]

while True:
    if triangle.ycor() >= 200:
        print("Triangle wins!")
        if triangle.ycor() > 200:
            triangle.setpos(-300, 200)
        triangle.pd
        triangle.begin_fill()
        triangle.rt(90)
        triangle.fd(25)
        for i in 1,2:
            triangle.lt(120)
            triangle.fd(50)
        triangle.lt(120)
        triangle.fd(25)
        triangle.end_fill()
        triangle.lt(90)
        triangle.hideturtle()
        break
    if circle.ycor() >= 200:
        print("Circle wins")
        if circle.ycor() > 200:
            circle.setpos(300, 225)
        circle.pd
        circle.begin_fill()
        circle.circle(25)
        circle.end_fill()
        circle.hideturtle()
        break
print("Triangle's turn: ")
    input("Press Enter to roll the die")
    die_outcome = random.choice(die)
    print("The result of the die roll is: ")
    print(die_outcome)
    print("The number of steps will be: ")
    print(20die_outcome)
    triangle.fd(20die_outcome)
    print("Circle's turn: ")
    input("Press Enter to roll the die")
    die_outcome = random.choice(die)
    print("The result of the die roll is: ")
    print(die_outcome)
    print("The number of steps will be: ")
    print(20die_outcome)
    circle.fd(20die_outcome)
