import turtle
import time

display_board = turtle.Screen()
display_board.bgcolor("light blue")
display_board.title("Catch the turtle")

def countdown(seconds):
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(0,300)
    turtle.color("dark blue")
    turtle.write('{:02d}:{:02d}'.format(00, seconds), align="center", font=("Arial", 48, "normal"))

    while seconds:
        time.sleep(1)
        seconds -= 1
        turtle.clear()
        turtle.write('{:02d}:{:02d}'.format(00, seconds), align="center", font=("Arial", 48, "normal"))

    turtle.clear()
    turtle.write("Game Over!", align="center", font=("Arial",48,"normal"))

countdown(10)
turtle.done()
