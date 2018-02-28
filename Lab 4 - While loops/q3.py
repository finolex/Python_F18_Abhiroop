dividend = int(input("Please input a positive int for dividend: "))
divisor = int(input("Please input a positive int for divisor: "))

count = 0
quotient = dividend


while quotient >= divisor:
    quotient -= divisor
    count += 1

print(count)
