n = input("Please enter a string with odd number of total characters: ")

mid = len(n)//2
midchar = n[mid]
uptomid = n[:mid]
frommid = n[mid+1:]

print("Middle character: ",midchar)
print("First Half: ",uptomid)
print("Second Half: ",frommid)
