userNumber = int(input("Please input a number that is less than 100: "))
L = int(userNumber/50)
total_2 = userNumber - L*50

X = int(total_2/10)
total_3 = userNumber - L*50 - X*10
V = int(total_3/5)

    
I = userNumber - L*50 - X*10 - V*5

print("L"*L, "X"*X, "V"*V, "I"*I)
