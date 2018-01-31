print('I can see the future.')
print('Give me a year in the future, and I\'ll guess the total population in the US then.')
years = int(input('Please enter the future year: '))
years_diff = years - 2018
seconds_diff = years_diff * 365 * 24 * 60 * 60
birth = int(seconds_diff/7)
death = int(seconds_diff/13)
immigrant = int(seconds_diff/35)
new_pop = 307357870 + birth - death + immigrant
print(new_pop)
