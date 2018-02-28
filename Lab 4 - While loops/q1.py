string1 = input("Please enter first string: ")
string2 = input("Please enter second string: ")

if len(string1) < len(string2):
    print(string1+string2+string1)
elif len(string2) < len(string1):
    print(string2+ string1+ string2)
else:
    print("error please try again")
