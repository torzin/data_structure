def gcd_extended(a, b):
    if a == 0:
        return 0, 1, b

    x1, y1, gcd = gcd_extended(b%a, a)

    x = y1 - (b//a)*x1
    y = x1

    return x, y, gcd


a, m = map(int, input().split())
inv, y, gcd = gcd_extended(a, m)  # Acha uma solução para a equação ax + my = 1
if gcd == m:
    print(-1)
else:
    print(inv % m)


