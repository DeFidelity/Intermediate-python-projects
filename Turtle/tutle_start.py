from turtle import Turtle, Screen, colormode
from random import choice,randint
tom = Turtle()
colormode(255)

def random_color():
    r = randint(0,255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    return color
tom.speed("fastest")

def draw_spirograph(gap_size):
    for _ in range(int(360 / gap_size)):
        tom.color(random_color())
        tom.circle(150)
        tom.setheading(tom.heading() + gap_size)

draw_spirograph(4)
# for _ in range(100):
#     tom.speed("fastest")
#     tom.color(random_color())
#     tom.circle(100)
#     tom.penup()
#     tom.right(50)
#     tom.pendown()
#     tom.circle(100)
# direction = [0, 90, 180, 270]
# tom.speed("fastest")
# tom.width(15)
#
#
# for _ in range(2500):
#     tom.color(random_color())
#     tom.forward(30)
#     tom.setheading(choice(direction))
# tim = Turtle()

# tim.shape("turtle")
# tim.color("blue")
# for me in range(4):
#     tim.forward(100)
#     tim.right(90)
# for u in range(10):
#     tom.forward(10)
#     tom.penup()
#     tom.forward(10)
#     tom.pendown()
#     tom.forward(10)
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tom.forward(100)
#         tom.right(angle)
#
# for shape_sides in range(3, 20):
# #     tom.color(choice(color))
#     draw_shape(shape_sides)


















screen = Screen()
screen.exitonclick()