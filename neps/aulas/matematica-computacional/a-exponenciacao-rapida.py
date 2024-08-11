
def ans(b, e, m):
    if e == 0:
        return 1 % m

    res = ans(b, e//2, m)
    res = (res*res) % m

    if e % 2 == 0:
        return res

    return (res*b) % m


b, e, m = map(int, input().split())
sol = ans(b, e, m)
print(sol)
