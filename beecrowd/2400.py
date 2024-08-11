n = int(input())
bit = [0] * (n+1)

vals = [0] + list(map(int, input().split()))
ans = 0


def setbit(pos, dif):
    global n
    while pos <= n:
        bit[pos] += dif
        pos += pos & -pos


def getbit(pos):
    new_ans = 0
    while pos:
        new_ans += bit[pos]
        pos -= pos & -pos
    return new_ans


for i in range(1, n+1):
    ans += (i - 1) - getbit(vals[i] - 1)
    setbit(vals[i], 1)

print(ans)
