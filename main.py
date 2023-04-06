import turtle as t
import random

tim = t.Turtle()

t.colormode(255)


tim.speed("fastest")

def draw_spi(size_of_gap):
    for _ in range(int(360/ size_of_gap)):
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spi(5)



screen = t.Screen()
screen.exitonclick()