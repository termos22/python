from turtle import *
import random

bgcolor("black")
colormode(255)
speed(0)

for x in range(500):
	r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
	pencolor(r, g, b)
	fd(x + 50)
	rt(91)
turtle.exitonclick()