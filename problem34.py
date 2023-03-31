def ft(n):
    if n == 0:
        return 1
    else:
        mult = 1
        while n != 1:
            mult *= n
            n -= 1
        return mult

