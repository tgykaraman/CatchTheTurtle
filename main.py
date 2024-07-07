import turtle
import tkinter as tk
import random
import time

#Ekranın düzenlenmesi
drawing_board = turtle.Screen()
drawing_board.title("Catch the Turtle Game")
drawing_board.bgcolor("lightblue")
drawing_board.setup(width=600,height=600)
drawing_board.tracer(0)

#Skor ve göstergeleri ayarlama
score = 0
game_duration = 15
end_time = time.time()+game_duration

#Skor
score_display = turtle.Turtle()
score_display.penup()
score_display.hideturtle()
score_display.goto(0,260)
score_display.write(f"Score: {score}", align="center", font=("Arial",24,"normal"))

#Timer
timer_display = turtle.Turtle()
timer_display.penup()
timer_display.hideturtle()
timer_display.goto(0,230)
timer_display.write("Timer: {:02d}:{:02d}".format(00, game_duration), align="center", font=("Arial",24,"normal"))

#Kaplumbağayı oluşturma ve hareket ettirme
turtle_object = turtle.Turtle()
turtle_object.shape("turtle")
turtle_object.penup()
turtle_object.color("green")


def game_over():
    drawing_board.clear()
    drawing_board.bgcolor("lightblue")
    game_over_display = turtle.Turtle()
    game_over_score_display = turtle.Turtle()
    game_over_display.penup()
    game_over_display.hideturtle()
    game_over_score_display.penup()
    game_over_score_display.hideturtle()
    game_over_display.goto(0,260)
    game_over_display.write(f"Game Over!", align="center", font=("Arial",36,"normal"))
    game_over_score_display.goto(0,230)
    game_over_score_display.write(f"Score:{score}", align="center", font=("Arial",36,"normal"))

def move_turtle():
    if time.time() < end_time:
        x = random.randint(-210,210)
        y = random.randint(-210,210)
        turtle_object.goto(x,y)
        turtle_object.speed(3)
        drawing_board.update()
        drawing_board.ontimer(move_turtle, random.randint(500,1000))
    else:
        turtle_object.hideturtle()
        game_over()

#Kaplumbağaya tıklayınca skoru arttırma
def increase_score(x,y):
    global score
    score += 1
    score_display.clear()
    score_display.write(f"Skor: {score}", align="center", font=("Arial", 24, "normal"))

turtle_object.onclick(increase_score)

def update_timer():
    remaining_time = int(end_time-time.time())
    if remaining_time > 0:
        timer_display.clear()
        timer_display.write("Timer: {:02d}:{:02d}".format(00, remaining_time), align="center", font=("Arial", 24, "normal"))
        drawing_board.ontimer(update_timer,1000)
    else:
        game_over()

move_turtle()
update_timer()

drawing_board.mainloop()