n = int(input("Please enter a positive integer: "))


for i in range(1,n+1):
    print((n-i)*".", i*str(i), sep="")
