def factorial(n):
    if n ==0:
        return 1
    fact = 1
    while n != 1:
        fact *= n
        n -= 1
    return fact


a = str(factorial(100))
b = []
for i in a:
    b.append(i)
sum = 0
for i in b:
    sum+=int(i)
print(sum)

