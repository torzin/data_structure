import math

n = int(input())
lim = int(math.sqrt(n)) + 1


def is_prime():
    for i in range(2, lim):
        if n % i == 0:
            return False
    return True


if n == 1:
    print('N')
elif is_prime():
    print('S')
else:
    print('N')
