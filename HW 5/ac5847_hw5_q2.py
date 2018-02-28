n = input("Please enter a single character: ")

if n.isdigit():
    print("You entered a number!")
elif n.isspace():
    print("You entered a space!")
elif n.isalpha():
    if n.lower() == n:
        print("You entered a lower case letter!")
    elif n.upper() == n:
        print("You entered an upper case letter!")
else:
    print("You entered a non-alphanumerical character!")
