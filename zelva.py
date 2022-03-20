import turtle
import random

triangle = turtle.Turtle()
triangle.shape("triangle")
triangle.pencolor("brown")

triangle.left(90)
triangle.penup()
triangle.goto(-300, -300)

circle = turtle.Turtle()
circle.shape("circle")
circle.pencolor("green")

circle.penup()
circle.goto(300, -300)

triangle.goto(-300, 200)
triangle.pendown()

triangle.right(90)
triangle.forward(25)

for i in range(2):
    triangle.left(120)
    triangle.forward(50)

triangle.left(120)
triangle.forward(25)

triangle.penup()
triangle.left(90)
triangle.goto(-300, -300)

circle.goto(300, 225)
circle.pendown()
circle.circle(25)
circle.penup()
circle.left(90)
circle.forward(25)
circle.right(90)
circle.goto(275, -300)

print("Begin!\n\n")
die = [1, 2, 3, 4, 5, 6]

for i in range(20):
    if triangle.pos() >= (-300, 200):
        print("\nTriangle wins!")
        break

    elif circle.pos() >= (300, 225):
        print("\nCircle wins\n")
        break

    else:
        triangle_turn = input("\nPress Enter to roll the die\n")
        die_outcome = random.choice(die)
        print("The result of the die roll is: ")
        print(die_outcome)
        print("The number of steps will be: ")
        print(20 * die_outcome)
        triangle.forward(20 * die_outcome)

        circle_turn = input("Press Enter to roll the die")

        die_outcome = random.choice(die)
        print("The result of the die roll is: ")
        print(die_outcome)
        print("The number of steps will be: ")
        print(20 * die_outcome)
        circle.fd(20 * die_outcome)

    if triangle.pos() >= (-300, 200):
        triangle.fillcolor("yellow")
        triangle.begin_fill()
        triangle.right(90)
        triangle.forward(25)

        for j in range(2):
            triangle.left(120)
            triangle.forward(50)

        triangle.left(120)
        triangle.forward(25)
        triangle.end_fill()

    elif circle.pos() >= (300, 225):
        circle.fillcolor("yellow")
        circle.begin_fill()
        circle.circle(25)
        circle.end_fill()
