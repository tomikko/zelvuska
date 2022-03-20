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

circle.left(90)
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

circle.goto(300, 200)
circle.right(90)
circle.pendown()
circle.circle(25)

circle.penup()
circle.left(90)
circle.goto(300, -300)

print("Begin!")
die = [1, 2, 3, 4, 5, 6]

while True:
    tri_y = triangle.ycor()
    cir_y = circle.ycor()

    if tri_y >= 200:
        print("\nTriangle wins!")

        triangle.fillcolor("yellow")
        triangle.pendown()
        triangle.begin_fill()
        triangle.right(90)
        triangle.forward(25)

        for j in range(2):
            triangle.left(120)
            triangle.forward(50)

        triangle.left(120)
        triangle.forward(25)
        triangle.end_fill()
        break

    if cir_y >= 200:
        print("\nCircle wins\n")

        circle.right(90)

        circle.fillcolor("yellow")
        circle.pendown()
        circle.begin_fill()
        circle.circle(25)
        circle.end_fill()
        break

    print("\n\nTriangle's turn:")
    input("Press Enter to roll the die\n")

    die_outcome = random.choice(die)
    tri_steps = 20 * die_outcome
    tri_num = (tri_y + tri_steps) - 200
    tri_neumimvymysletnazvyprostepresah = (tri_num / abs(tri_num) + 1) / 2 * tri_num

    print("The result of the die roll is: ")
    print(die_outcome)
    print("\nThe number of steps will be:")
    print(tri_steps)
    triangle.forward(tri_steps - tri_neumimvymysletnazvyprostepresah)

    print("\nCircle's turn:")
    input("Press Enter to roll the die\n")

    die_outcome = random.choice(die)
    cir_steps = 20 * die_outcome
    cir_num = (cir_y + cir_steps) - 200
    cir_neumimvymysletnazvyprostepresah = (cir_num / abs(cir_num) + 1) / 2 * cir_num

    print("The result of the die roll is: ")
    print(die_outcome)
    print("\nThe number of steps will be: ")
    print(cir_steps)
    circle.forward(cir_steps - cir_neumimvymysletnazvyprostepresah)
