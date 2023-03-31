def sum_of_squares(n):
    s = 0
    for i in range(0, n):
        s += i * i
    return s


print(sum_of_squares(101))


def square_of_sums(n):
    s = 0
    for i in range(0, n):
        s += i ** 3
    return s


print(square_of_sums(101))

print(square_of_sums(101) - sum_of_squares(101))
