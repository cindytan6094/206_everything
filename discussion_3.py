# Name: Cindy Tan
# UMID: 05337104
from turtle import *

### write all new functions here ###

def circle(turtle, r=50):
    turtle.circle(r)

def draw_emoji(turtle):
    turtle.pencolor('yellow')
    turtle.fillcolor('yellow')
    turtle.goto(0,-50)
    turtle.begin_fill()
    circle(turtle, 150)
    turtle.end_fill()
    turtle.penup()
    turtle.pencolor('black')
    turtle.fillcolor('black')
    turtle.goto(-50,120)
    turtle.pendown()
    turtle.begin_fill()
    circle(turtle, 10)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(50,120)
    turtle.pendown()
    turtle.begin_fill()
    circle(turtle, 10)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(-50,30)
    turtle.pencolor('black')
    turtle.pensize(5)
    turtle.pendown()
    turtle.left(20)
    turtle.forward(120)

    """
    Write a function to draw an emoji.
    """

    

def main():
    """
    Make sure to create a Screen object, a Turtle object,
    and call draw_emoji.

    Also, make sure to call the .exitonclick() method on your Screen instance
    to stop the program from exiting until you close the drawing window.

    TIP: You can call the .bgcolor() method on your Screen instance to change
    the background color.

    """
    space = Screen()
    space.bgcolor('light gray')
    smile = Turtle()
    draw_emoji(smile)
    space.exitonclick()
    
    


if __name__ == '__main__':
    main()


