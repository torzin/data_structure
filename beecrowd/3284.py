n = int(input())

bit = [0] * (n+1)
vals = [0] + list(map(int, input().split()))

ans = 0


def setbit(pos, diff):
    while pos <= n:
        if pos % 2 == 0:
            bit[pos] += diff
            break
        bit[pos] += diff
        pos += pos & -pos


def getbit(pos):
    new_ans = 0
    while pos:
        new_ans += bit[pos]
        pos -= pos & -pos
    return new_ans


for i in range(1, n+1):
    setbit(i, vals[i])


for k in range(1, n-1):
    if vals[k] > vals[k+2]:
        setbit(k, vals[k+2]-vals[k])
        setbit(k+2, vals[k]-vals[k+2])
        ans += 1

print(ans)

