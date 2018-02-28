n = int(input("Please enter a positive integer: "))

x = 1
y = 0
for i in (1,n):
    while(2*n-x) >= 1:
        print(y*" "+(2*n-x)*"*", sep="")
        y+=1
        x+=2

x = 1
y = n-1
for i in (1,n):
    while x < 2*n:
        print(y*" "+x*"*", sep="")
        y-=1
        x+=2
