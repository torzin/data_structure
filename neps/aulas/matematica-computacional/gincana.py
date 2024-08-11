a1, a2 = map(int, input().split())


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

X = a2
while gcd(X, a1) > 1:
    X -= 1

print(X)
