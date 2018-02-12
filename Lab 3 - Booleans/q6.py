sides = int(input("Please enter the number of sides for your shape (between 3 and 5): "))

if sides == 3:
    print("Your shape is a triangle.")
    
elif sides == 5:
    print("Your shape is a pentagon.")
    
elif sides == 4:
    equal = input("Are your sides of equal length? Please enter Y or N: ")
    degrees = input("Are all angles 90 degrees? Please enter Y or N: ")
    
    if equal.upper() == "Y" and degrees.upper() == "Y":
       print("Your shape is a square.")
    elif equal.upper() == "N" and degrees.upper() == "N":
       print("Your shape is a quadrilateral.")
    elif equal.upper() == "Y" and degrees.upper() == "N":
       print("Your shape is a quadrilateral.")
    elif equal.upper() == "N" and degrees.upper() == "Y":
       print("Your shape is a rectangle.")
    else:
       print("Please try again.")
       
else:
    print("Please try again.")
