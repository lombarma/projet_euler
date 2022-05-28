def reste_nul(a, b):
    return True if a % b == 0 else False
#print(reste_nul(2520, 10))
#1 2 3 4 5 6 7 8 9 10

start = 1
b = 1
while start != 21:
    if reste_nul(b, start):
        start+=1
    else:
        start=1
        b+=1
print(b)
