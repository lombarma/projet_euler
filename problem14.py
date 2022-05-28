def even_number(n):
    return n / 2


def odd_number(n):
    return 3 * n + 1


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


compteur = 0
maximum = compteur

for i in range(0, 1000000):
    while i != 1:
        if is_even(i):
            even_number(i)
            compteur += 1
        elif not is_even(i):
            odd_number(i)
            compteur += 1
    if compteur > maximum:
        maximum = compteur
print(compteur)
