string1 = input("Please enter a string to check if palindrome: ")

if string1[::-1] == string1:
    print("This is a palindrome!")
else:
    print("This is not a palindrome")
