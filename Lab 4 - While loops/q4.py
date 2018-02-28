dividend = int(input("Please input a positive int for dividend: "))
divisor = int(input("Please input a positive int for divisor: "))

remainder = dividend

while remainder >= divisor :
    remainder -=  divisor


print(remainder)
