def is_palindrome(num):
    num = str(num)
    pal_len = len(num)
    a = ""
    b = ""
    if pal_len % 2 == 0:
        a = num[0:int(pal_len / 2)]
        b = num[int(pal_len / 2):]
    else:
        a = num[0:int(pal_len / 2 + 1 / 2)]
        b = num[int(pal_len / 2 + 1 / 2 - 1):]
    return True if a == b[::-1] else False


def mult_all():
    start = 100
    list_numbers = []
    while len(str(start)) != 4:
        for i in range(100, 1000):
            list_numbers.append(start * i)
        start += 1
    return set(list_numbers)


# print(mult_all())


def list_pal(set_type):
    a = []
    for i in set_type:
        if is_palindrome(i):
            a.append(i)
    return a


# print(list_pal(mult_all()))

def max_list(liste):
    liste = sorted(liste, reverse=True)
    return liste[0]


print(max_list(list_pal(mult_all())))

"""a = 1
b = []
c =0
while len(str(a)) != 3:
    for i in range(0, 11):
        c = a*i
        b.append(c)
    a+=1
print(b)"""
