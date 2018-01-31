print('Please enter your amount in the format of dollars and cents in two separate lines: ')
dollars = int(input())
cents = int(input())
total = dollars*100 + cents
quarters = int(total/25)
total_2 = total - quarters*25
dimes = int(total_2/10)
total_3 = total - quarters*25 - dimes*10
nickels = int(total_3/5)
total_4 =total - quarters*25 - dimes*10 - nickels*5
pennies = int(total_4)
print(quarters, "quarters, ", dimes, "dimes, ", nickels, "nickels, ", pennies, "pennies.")
