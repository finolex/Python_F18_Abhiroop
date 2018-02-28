print("Let me calculate the cost of your call for me :)")

start = int(input("Please enter the time of start of your call in 24hr format ie. 1330 for 1.30pm: "))
duration = int(input("Please enter duration of your call in minutes: "))            
day = input("Please enter the first 3 letters of the day of week you made the call ie. mon, tue, wed..: ")

            
if ((day == "mon" or day == "tue" or day == "wed" or day == "thu" or day == "fri") and start < 800) or ((day == "mon" or day == "tue" or day == "wed" or day == "thu" or day == "fri") and start > 1800):
    total = duration*0.25
elif ((day == "mon" or day == "tue" or day == "wed" or day == "thu" or day == "fri") and start >= 800) or ((day == "mon" or day == "tue" or day == "wed" or day == "thu" or day == "fri") and start <= 1800): 
    total = duration*0.40
elif day == "sat" or day == "sun":
    total = duration*0.15
else:
    print("Please try again.")


print("Your total cost is: $", total)
