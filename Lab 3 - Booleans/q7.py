s = int(input("Please enter your time in 24hr format (such as 1337 for 13:37): "))

hours = s//100
minutes = s - hours*100

if s - 1200 < 0:
    if minutes < 10:
        minutes = "0" + str(minutes)
    print(hours,":",minutes, "in 12 hour format is ", hours,":",minutes, "am.")
    
elif s - 1200 >= 0 and s - 1200 < 100:
    if minutes < 10:
        minutes = "0" + str(minutes)
    print("test")
    print(hours,":",minutes, "in 12 hour format is ", hours,":",minutes, "pm.")
    
elif s - 1200 >= 100 and s - 1200 <= 1159:
    hoursNew = hours - 12
    print(hoursNew)
    if minutes < 10:
        minutes = "0" + str(minutes)
    print(hours,":",minutes, "in 12 hour format is ", hoursNew,":",minutes, "pm.")
elif s - 1200 == 1200:
    hoursNew = hours - 12
    if minutes < 10:
        minutes = "0" + str(minutes)
    print(hours,":",minutes, "in 12 hour format is ", hoursNew,":",minutes, "am.")

else:
    print("Please try again.")
