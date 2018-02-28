n1 = int(input("Please enter the first number: "))
n2 = int(input("Please enter the second number for comparison: "))

counter = 0

for i in range(0  , n1):
    if (n1//(10**i) - n2//(10**i)) != 10 and (n1//(10**i) - n2//(10**i)) != 0:
        counter += 1

print(counter)


while n1 > 0:
    if n1%10 != n2%10:
        counter += 1
    n1 = n1//10
    n2= n2//10


