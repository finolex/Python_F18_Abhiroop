import random

n = random.randint(1,100)
print("I have thought of a random number between 1 and 100, take your guess :)")
x = 0

while x != n:
    x = int(input("What is your guess?: "))
    if x < n:
        print("Your guess is too small. Try larger!")
    elif x > n:
        print("Your guess is too large. Try smaller!")

print("You guessed the number!")
