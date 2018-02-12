import math

firstLeg = int(input("Please enter the length of the first leg: "))
secondLeg = int(input("Please enter the length of the second leg: "))
hyp = float(input("Please enter the length of the hypothenuse: "))

hypCalc = math.sqrt(firstLeg**2 + secondLeg**2)

if hyp == hypCalc:
    print("This forms a right angled triangle!")
elif abs(hyp - hypCalc) < 0.00001:
    print("This forms a right angled triangle!")
else:
    print("This does not form a right angled triangle.")


