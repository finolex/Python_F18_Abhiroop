DOB = int(input("Please enter your DOB in the format YYYYMMDD: "))
date = int(input("Please today\'s date in the format YYYYMMDD: "))

##this is for DOB

year_DOB = DOB//10000
total_2 = DOB - year_DOB*10000

month_DOB = total_2//100
total_3 = total_2 - month_DOB*100

day_DOB = total_3

print(month_DOB,"/",day_DOB,"/",year_DOB)

## This is for date

year_date = date//10000
total_2_d = date - year_date*10000

month_date = total_2_d//100
total_3_d = total_2_d - month_date*100

day_date = total_3_d

print(month_date,"/",day_date,"/",year_date)

## this is for start number of days

start_days = year_DOB*12*30 + month_DOB*30 + day_DOB
current_days = year_date*12*30 + month_date*30 + day_date
diff_days = current_days - start_days

years_age = diff_days//(12*30)
total_2_a = diff_days - years_age*(12*30)
months_age = total_2_a//30
total_3_a = total_2_a - months_age*30
days_age = total_3_a

print("Your age is ", years_age, "years, ", months_age, "months and ", days_age, "days.")
