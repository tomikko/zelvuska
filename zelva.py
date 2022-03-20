import turtle
import random
triangle = turtle.Turtle()
triangle.shape("triangle")
triangle.pencolor("brown")
triangle.lt(90)
triangle.pu()
triangle.goto(-300, -300)
circle = triangle.clone()
circle.shape("circle")
circle.pencolor("green")
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

for i in range(20):
    if triangle.pos() >= (-300, 200):
        print("triangle wins")
        break
    elif circle.pos() >= (300, 225):
        print("circle wins")
        break
    else:
           triangle_turn = input("Press Enter to roll the die")
           die_outcome = random.choice(die)
           print("The result of the die roll is: ")
           print(die_outcome)
           print("The number of steps will be: ")
           print(20*die_outcome)
           triangle.fd(20*die_outcome)
           circle_turn = input("Press Enter to roll the die")
           die_outcome = random.choice(die)
           print("The result of the die roll is: ")
           print(die_outcome)
           print("The number of steps will be: ")
           print(20*die_outcome)
           circle.fd(20*die_outcome)

    if triangle.pos() >= (-300, 200):
        triangle.fillcolor("yellow")
        triangle.begin_fill()
        triangle.rt(90)
        triangle.fd(25)
        for i in 1,2:
            triangle.lt(120)
            triangle.fd(50)
        triangle.lt(120)
        triangle.fd(25)
        triangle.endf_fill()
    elif circle.pos() >= (300, 225):
        circle.fillcolor("yellow")
        circle.begin_fill()
        circle.circle(25)
        circle.end_fill()
