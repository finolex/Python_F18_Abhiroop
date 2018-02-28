import turtle
import math

n = int(input("Please enter a number of sides in your polygon: "))

angle = 360/n

for i in range(n):
    turtle.forward(100)
    turtle.left(angle)
