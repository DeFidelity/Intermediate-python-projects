from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)
def move_backward():
    tim.backward(10)
def clock():
    hi = tim.heading() + 10
    tim.setheading(hi)
def anti_clock():
    hi = tim.heading() + 10
    tim.setheading(hi)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()




screen.listen()
screen.onkey(key="a", fun=clock)
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(anti_clock(), "d")
screen.onkey(clear, "c")










screen.exitonclick()


# mini calc for the culture
# def add(n1,n2):
#     return n1 + n2
# def subtract(n1,n2):
#     return n1 - n2
#
# def do_the_work(n1,n2,func):
#     return func(n1, n2)
#
# work = do_the_work(2,3,add)
# print(work)