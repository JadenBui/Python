import turtle  # to import the turtle module
import random  # to import the random module
import math  # to import the math module
colors = ["red", "yellow", "lightgreen", "orange"]  # create a color list
colorss = ["red", "yellow", "lightgreen", "orange", "blue", "lightblue", "purple", "green",
           "orange", "lightyellow", "grey", "violet"]  # create a color list for the polygon.
# CREATE AN ABSTRACT FLOWER


def rectangle(t, n, m):  # a rectangle is drawn by turtle t with the width of n , length of m
    t.forward(n/2)
    t.right(90)
    t.forward(m)
    t.right(90)
    t.forward(n)
    t.right(90)
    t.forward(m)
    t.right(90)
    t.forward(n/2)


def turtle_pistil(t):  # the flower pistil is drawn by turtle t
    t.goto(1, 1)  # cordinate (1,1) is set to be the center of the flower
    a = 0  # The original value will be 0
    # Frist layer has 6 turtles, the following layer has 6+7 turtles and so on.An arithmetic sequence of 7 is set to complete the pistil.
    for i in range(6, 34, 7):
        for l in range(i):  # To put on the number of turtle in each layer
            # To change the color of the turtle layer one by one followed the color in the string list
            t.color(colors[a])
            t.penup()
            # The distance of each layer stays the same so we use multiplication with the unfixed varible.
            t.forward(22*(a+1))
            t.stamp()
            t.back(22*(a+1))
            # To create a circle of turtle , each turtle will present a line of angle, so we devide the total angle of the circle by the number of turtle.
            t.left(360/i)
        a += 1  # The varible will be added up by 1 unit for each loop


def draw_petal(t, x, y):  # x is the width and y is the length of the petal drawn by turtle t
    a = 0  # The original varible is 0
    # to advoid the petal and the pistil having the same color
    random.shuffle(colors)
    for m in range(4):  # to draw 4 types of color of a petal
        # fill the color for each of the petal and the color is changed 4 times in order of the colors list
        t.fillcolor(colors[m])
        t.begin_fill()  # start to fill color
        # the angle between each petal(different color) is 360/48 with 360 is the total degree of the circle,48 is the number of petal
        t.right(7.5)
        t.goto(1, 1)  # back to the center
        a += 1  # The varible will be added up by 1 unit for each loop
        for i in range(12):  # there are 12 petal of each color, so each color will have 12 petals
            t.penup()
            # the number of the distance between the center and the petal
            t.forward(95)
            t.pendown()
            t.left(90)
            rectangle(t, x, y)
            # to turn the direction of the turtle back to the original direction
            t.right(90)
            t.penup()
            t.goto(1, 1)
            t.right(30)  # an angle to create 12 petals of each color
            a += 1  # The varible will be added up by 1 unit for each loop
        t.end_fill()
    t.goto(1, 1)


def flw_body(t):
    t.penup()
    t.color("green")  # A body of the flower will be drawn by turtle t
    # a position that i chose to make the body(the body will be drawn from the center but start from the lower position)
    t.goto(1, -96)
    t.pendown()
    t.fillcolor("green")
    t.begin_fill()
    rectangle(t, 90, 300)
    t.end_fill()
    t.penup()
# CREATE POLYGONS SPIRAL


def polygons(t, o, p):  # polyogons will bi drawn by turtle t with o sides and p area
    # the side_length formular
    side_length = math.sqrt(p/o * 4 * math.tan(math.pi/o))
    t.turtlesize(0.5)
    for i in range(o):  # to draw the number of side the polygon has
        t.forward(side_length/2)
        t.stamp()
        t.forward(side_length/2)
        t.left(360/o)


def polygons_spiral(t, p):
    for o in range(20, 2, -1):  # to create a spiral of 20 polygons
        side_length = math.sqrt(p/o * 4 * math.tan(math.pi/o))
        t.fillcolor(random.choice(colorss))  # to choose a random color
        t.begin_fill()
        polygons(t, o, p)
        t.end_fill()
        t.penup()
        t.forward(side_length/2)
        t.pendown()
        t.right(30)


# main fuction
while True:  # create an ìnfinite printing loop
    print("""*************************
1. Draw Spiral of Polygons
2. Draw an Abstract flower
3. Exit
*************************""")
    option = input("Please enter an option (1/2/3):   ")
    if option == "1":

        win = turtle.Screen()
        win.clear()
        win.bgcolor("white")
        tito = turtle.Turtle()
        tito.shape("arrow")
        tito.speed("fastest")
        polygons_spiral(tito, 30000)

    elif option == "2":
        win = turtle.Screen()
        win.clear()
        win.bgcolor("white")
        tito = turtle.Turtle()
        tito.shape("turtle")
        tito.speed("fastest")
        flw_body(tito)
        turtle_pistil(tito)
        draw_petal(tito, 40, 200)

    elif option == "3":
        print("Program exits. Have a nice day!")
        break  # to break the infinite loop
