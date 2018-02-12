J_days = int(input("Please enter number of days John worked: "))
J_hours = int(input("Please enter number of hours John worked: "))
J_minutes = int(input("Please enter number of minutes John worked: "))

B_days = int(input("Please enter number of days Bill worked: "))
B_hours= int(input("Please enter number of hours Bill worked: "))
B_minutes = int(input("Please enter number of minutes Bill worked: "))

total = J_days*60*24 + J_hours*60 + J_minutes + B_days*60*24 + B_hours*60 + B_minutes

t_days = total//(60*24)

total2 = total - t_days*60*24

t_hours = total2//60

total3 = total2 - t_hours*60

t_minutes = total3

print("The total time they worked together is ", t_days, "days ", t_hours, "hours and ", t_minutes, "minutes.")
