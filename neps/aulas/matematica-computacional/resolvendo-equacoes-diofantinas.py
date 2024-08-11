def gcd_extended(a, b):
    if a == 0:
        return 0, 1, b

    x1, y1, gcd = gcd_extended(b%a, a)

    x = y1 - (b//a) * x1
    y = x1

    return x, y, gcd


def find_solutions(a, b, c):
    if a == 0 and b == 0:
        if c == 0:
            return True, 0, 0
        else:
            return False, 0, 0

    x, y, gcd = gcd_extended(a, b)

    if a < 0:
        x = -x
    if b < 0:
        y = -y

    if c % gcd != 0:  # checa se existe alguma solução
        return False, 0, 0

    t = c // gcd
    return True, x*t, y*t


a, b, c = map(int, input().split())
found, x, y = find_solutions(a, b, c)
if found:
    print(1)
    print(f'{x} {y}')
else:
    print(-1)




