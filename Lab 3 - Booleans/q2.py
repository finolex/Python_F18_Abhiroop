name = input("Please enter your name: ")
gYear = input("Please enter a graduation year: ")
cYear = input("Please enter the current year: ")

diff = int(gYear) - int(cYear)

if diff < 0:
    status = "graduated."
elif diff == 0:
    status = "a senior."
elif diff == 1:
    status = "a junior."
elif diff == 2:
    status = "a sophomore."
elif diff == 3:
    status = "a freshman."
elif diff > 3:
    status = "not in college yet."
else:
    print("Error, please try again")


print(name, "is ", status)
