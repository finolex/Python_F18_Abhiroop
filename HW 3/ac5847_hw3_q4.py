import math

print("I will try to solve a quadratic equation for you!")

a = float(input("Please enter your first number as a decimal: "))
b = float(input("Please enter your second number as a decimal: "))
c = float(input("Please enter your third number as a decimal: "))

test = b**2 -(4*a*c)

if a == 0 and b == 0 and c == 0:
    print("This has infinite solutions.")
elif a == 0 and b == 0:
    print("This has no solution.")
elif test < 0:
    print("This has no real solutions.")
elif test > 0:
    solution1 = ((-b + math.sqrt(test))/2*a)
    solution2 = ((-b - math.sqrt(test))/2*a)
    if solution1 == solution2:
        print("This has 1 real solution, and that value is ", solution1)
    else:
        print("This has 2 real solutions, and the values are ", solution1, "and ", solution2)
else:
    print("Error, please try again thanks!")
