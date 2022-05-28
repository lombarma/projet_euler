def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

resultat = 2
for i in range(3, 2000000, 2):
    if is_prime(i):
        resultat += i
print(resultat)