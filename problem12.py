def factors(n):
    factor_list = []
    for i in range(1, n + 1):
        if n % i == 0:
            factor_list.append(i)
    return factor_list


def triangle_numbers(n):
    liste = []
    cpt = 0
    while n != 0:
        cpt+=n
        n -= 1
    liste.append(cpt)
    return liste

print(triangle_numbers(9))
