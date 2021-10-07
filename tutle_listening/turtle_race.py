from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(height=400, width=500)
user_guess = screen.textinput(title="choose your winner", prompt="which turtle s going to win the race? ")
if user_guess:
    is_race_on = True
colors = ["red", "orange", "yellow", "blue", "purple", "gold"]
y = [-70, -40, -10, 20, 50, 80]
all_turtle = []

for turtle_index in range(0, 6):
    new_tutle = Turtle(shape="turtle")
    new_tutle.penup()
    new_tutle.goto(x=-230, y=y[turtle_index])
    new_tutle.color(colors[turtle_index])
    all_turtle.append(new_tutle)
while is_race_on:

    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_guess:
                print(f"You've won! The {winning_color} tutle is the winner!")
            else:
                print(f"You've lost! The {winning_color} tutle is the winner!")
        move_by = random.randint(6,10)
        turtle.forward(move_by)
screen.exitonclick()
