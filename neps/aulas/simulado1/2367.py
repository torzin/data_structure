import math

n, e, d = map(int, input().split())

min_val = math.inf

for i in range(n):
    ei, di = map(int, input().split())
    ac_val = abs(ei - e) + abs(di - d)

    if ac_val < min_val:
        min_val = ac_val

print(min_val)
