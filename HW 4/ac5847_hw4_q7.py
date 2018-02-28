import random

n = random.randint(1,100)
print(n)
print("I have thought of a random number between 1 and 100, take your guess :)")
largelimit = 100
smalllimit = 1
x = 0
life = 6
while x != n:
    life -= 1
    if life != 0:
        print("Range: [", smalllimit, ",", largelimit,"]. You have", life, "guesses left.")     
        x = int(input("What is your guess?: "))
        if x < n:
            print("Your guess is too small. Try larger!")
            smalllimit = x
        elif x > n:
            print("Your guess is too large. Try smaller!")
            largelimit = x
    else:
        print("You ran out of guess(es). The answer was", n)
        break;
    

if life !=0:
    print("You guessed the number! You guessed it in", (5-life), "guess(es) only!")
