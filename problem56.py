somme = 0
maximum = 0


def sum_numbers(n):
    a = [int(i) for i in str(n)]
    return sum(a)


for a in range(0, 100):
    for b in range(0, 100):
        if sum_numbers(a**b) > maximum:
            maximum = sum_numbers(a**b)
print(maximum)
