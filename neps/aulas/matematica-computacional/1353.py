import sys

sys.set_int_max_str_digits(10**5)
sys.setrecursionlimit(10**8)

def fast_expo(b, e, m):
    if e == 0:
        return 1 % m

    res = fast_expo(b, e//2, m)
    res = (res*res) % m

    if e % 2 == 0:
        return res

    return (res*b) % m


b = int(input())
e = int(input())
m = int(input())

ans = fast_expo(b, e, m)
print(ans)