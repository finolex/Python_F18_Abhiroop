num1 = int(input("Please enter your first integer: "))
num2 = int(input("Please enter your second integer: "))

if num2 == 0:
    print("This has no solutions.")
elif (-num1/num2) > 0 or (-num1/num2) < 0:
    print("This has a single solution and x = .", (-num1/num2))
elif (-num1/num2) == 0:
    print("This has a single solution.")
else:
    print("This has infinite solutions.")
