import math

item1 = float(input("Please input price of first item without dollar sign, and to 2dp: "))
item2 = float(input("Please input price of second item without dollar sign, and to 2dp: "))

print("There is an offer for buying 2 items! You get the lower priced item at 50% off!")

card = input("Are you a card member? Enter with y for yes and n for no: ")
tax = float(input("Please enter tax percentage as a 2dp number without the % sign: "))
if item1 < item2:
    total = 0.5*item1 + item2
elif item1 > item2:
    total = item1 + 0.5*item2
elif item1 == item2:
    total = 0.5*item1 + item2
else:
    print("Error try again!")

if card == "y":
    total2 = total*0.9
elif card == "n":
    total2 = total

total3 = round(((1+(tax/100))*total2),2)

print("Your Base price is = $", round(item1 + item2,2))
print("Your price after discounts = $", round(total2,2))
print("Your total for the 2 items based on your entered information is: $", total3)

