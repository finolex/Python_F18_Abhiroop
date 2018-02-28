total = 0
counter = 1
n = "placeholder"
print("Please enter a non-empty sequence of positive integers, each one in a separate line. End your sequence by typing done!")

while n != "done":
    n = input("")
    if n != "done":
        total += int(n)
    counter += 1

print("The geometric mean = ", total**(1/counter))
