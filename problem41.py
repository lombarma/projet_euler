import math
import itertools
def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    else:
        for i in range(5, int(math.sqrt(n)) + 1, 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False
        return True


unique_numbers = [1, 12, 123, 1234, 12345, 123456, 1234567, 12345678, 123456789]
unique_numbers = [str(i) for i in unique_numbers]

new = []
for i in unique_numbers:
    new.append(["".join(j) for j in list(itertools.permutations(i))])
l=[]
for i in new:
    l.extend(i)
l=[int(i) for i in l]
print(max([i for i in l if is_prime(i)]))


# range : 987654321
