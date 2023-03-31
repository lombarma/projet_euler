def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# problem35 project euler

def main():
    count = 0
    for i in range(2, 1000000):
        if is_prime(i):
            if str(i) == str(i)[::-1]:
                count += 1
    print(count)

main()