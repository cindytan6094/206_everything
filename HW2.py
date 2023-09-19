# Your name: Cindy Tan
# Your student id: 05337104
# Your email: cindytan@umich.edu
# List who or what you worked with on this homework: https://docs.python.org/3/library/turtle.html
# If you used generative AI also include how you used it.

# import the turtle functions for use in this program
# don't need to use the module name

from turtle import *
import random

def circle(turtle, fill_color='white', x=0, y=0, r=50):
    turtle.penup()
    turtle.goto(x, y - r)
    turtle.pendown()
    turtle.fillcolor(fill_color)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()

def rectangle(turtle, fill_color='black', x=0, y=0, width=50, height=100):
    turtle.penup()
    turtle.goto(x - width/2, y)
    turtle.pendown()
    turtle.fillcolor(fill_color)
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

def triangle(turtle, fill_color='orange', x=0, y=-50, size=20):
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(-60)
    turtle.pendown()
    turtle.fillcolor(fill_color)
    turtle.begin_fill()
    for i in range(3):
        turtle.forward(size)
        turtle.left(120)
    turtle.end_fill()



def draw_scene(turtle):
    # Snowman body parts
    circle(turtle, 'white', 0, -175, 100)  # bottom snowman body
    circle(turtle, 'white', 0, -55, 75)   # middle snowman body
    circle(turtle, 'white', 0, 60, 50)    # top snowman body

    # Snowman hat parts

    rectangle(turtle, 'black', 0, 110, 70, 40)   # snowman hat top part
    rectangle(turtle, 'black', 0, 105, 100, 15)  # snowman hat bottom part

    # Snowman face details
    circle(turtle, 'black', -15, 85, 5)  # left eye
    circle(turtle, 'black', 15, 85, 5)   # right eye
    triangle(turtle, 'orange', -5, 70, 15) # nose

    # Snowman buttons
    circle(turtle, 'black', 0, -35, 5)   # top button
    circle(turtle, 'black', 0, -60, 5)   # middle button
    circle(turtle, 'black', 0, -85, 5)   # bottom button

    # Snowman arms
    turtle.penup()
    turtle.goto(70, -20)
    turtle.setheading(135)
    turtle.pendown()
    turtle.pensize(10)
    turtle.pencolor('brown')
    turtle.right(75)
    turtle.forward(75)

    turtle.penup()
    turtle.goto(-70, -20)
    turtle.setheading(-135)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(75)

    # Snow particles
    turtle.pencolor('white')
    for i in range(20):
        turtle.penup()
        turtle.goto(random.randint(-300, 300), random.randint(0, 300))
        turtle.pendown()
        turtle.fillcolor('white')
        turtle.begin_fill()
        circle(turtle, 'white', x=turtle.xcor(), y=turtle.ycor(), r=3)
        turtle.end_fill()


def main():
    space = Screen()
    space.bgcolor('light blue')
    snowman = Turtle()
    snowman.speed(5)
    draw_scene(snowman)
    space.exitonclick()

if __name__ == '__main__':
    main()
