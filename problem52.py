def function(n):
    liste = [int(i) for i in str(n)]
    liste_tri = sorted(liste)
    return liste_tri


def function1():
    for i in range(1, 100000000000):
        if function(i) == function(2 * i) == function(3 * i) == function(4 * i) == function(5 * i) == function(6 * i):
            return i


print(function1())
