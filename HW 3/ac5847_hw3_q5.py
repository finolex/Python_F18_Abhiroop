import math

print("Let me guess the type of your triangle.")

side1 = float(input("Enter length of first side of triangle: "))
side2 = float(input("Enter length of second side of triangle: "))
side3 = float(input("Enter length of third side of triangle: "))

if side1 == side2 and side1 == side3:
    print("This is an equilateral triangle!")
elif side1 == side2 or side1 == side3 or side2 == side3:
    angle1 = math.acos((side1**2 + side2**2 - side3**2)/(2*side1*side2))
    angle2 = math.acos((side2**2 + side3**2 - side1**2)/(2*side2*side3))
    angle3 = math.acos((side3**2 + side1**2 - side2**2)/(2*side3*side1))
    if abs(angle1-90) < 0.00001 or abs(angle2-90) < 0.00001 or abs(angle3-90) < 0.00001:
        print("This is an isosceles right angle triangle.")
    else:
        print("This is an isosceles triangle and not right angled.")
else:
    print("This is neither an equilateral nor an isosceles triangle.")
