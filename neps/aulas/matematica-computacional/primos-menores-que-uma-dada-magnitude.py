import math

n = int(input())
ans = []


def is_prime(n):
    lim = int(math.sqrt(n)) + 1
    for i in range(2, lim):
        if n % i == 0:
            return False
    return True


for i in range(2, n+1):
    if is_prime(i):
        print(i, end=' ')
