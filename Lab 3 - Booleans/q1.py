entry = input("Please enter a es, or en, or an odd/even number: ")

if entry == "en":
    print("English")

elif entry == "es":
    print("Espanol")
elif (int(entry)%2 == 0):
    print("This is an even number")
elif (int(entry)%2 == 1):
    print("This is an odd number")
else:
    print("Error. Please type in an appropriate format")
