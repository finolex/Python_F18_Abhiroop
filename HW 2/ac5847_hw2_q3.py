import math
import turtle

line1 = int(input("Please enter length of first edge of triangle: "))
line2 = int(input("Please enter length of second edge of triangle: "))
angle1 = int(input("Please enter angle between edges of triangle in degrees: "))

turtle.forward(line1)
turtle.left(180-angle1)
turtle.forward(line2)

line3 = math.sqrt((line1**2) + (line2**2) - (2*line1*line2*math.cos(math.radians(angle1))))
angle2 = math.degrees(math.asin(line1*math.sin(math.radians(angle1))/line3))

turtle.left(180-angle2)
turtle.forward(line3)
print(angle2, line3)


