print('Please enter number of coins: ')
quarters = int(input('# of quarters '))
dimes = int(input('# of dimes '))
nickels = int(input('# of nickels '))
pennies = int(input('# of pennies '))
total = quarters*25 + dimes*10+  nickels*5 + pennies*1
cents = total%100
dollars = int((total - cents)/100)
print('The total is ', dollars, "dollars and ", cents, "cents")
