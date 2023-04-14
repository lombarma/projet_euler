def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(is_prime(495))

list_of_prime = []
a = 0
while len(list_of_prime) != 10002:
    if is_prime(a):
        list_of_prime.append(a)
    a+=1

print(list_of_prime[10001])