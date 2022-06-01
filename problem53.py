def factorielle(n):
    if n in range(0, 2):
        return 1
    else:
        compteur = 1
        while n != 1:
            compteur *= n
            n -= 1
        return compteur


def k_parmi_n(k, n):
    if k <= n:
        return factorielle(n) / (factorielle(k) * factorielle(n - k))


compteur = 0
"""for i in range(1, 101):
    if k_parmi_n(10, i) >= 1000000:
        compteur += 1
print(compteur)"""

for i in range(1, 101):
    for j in range(0, i+1):
        if k_parmi_n(j, i) >= 1000000:
            compteur+=1
print(compteur)