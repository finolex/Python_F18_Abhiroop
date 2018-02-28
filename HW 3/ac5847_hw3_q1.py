weight = int(input("Please enter your weight in kilograms: "))
height = float(input("Please enter your height in meters, in 2 decimal places: "))
bmi = weight/height**2
print("Your BMI is: ", bmi)

if bmi < 18.5:
    print("You are underweight")
elif bmi >= 18.5 and bmi <= 24.9:
    print("You are normal")
elif bmi >= 25 and bmi <=29.9 :
    print("You are overweight")
elif bmi >= 30:
    print("You are obese")
else:
    print("Error please try again!")
