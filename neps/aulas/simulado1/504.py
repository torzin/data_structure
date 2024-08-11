import math


c, t = map(int, input().split())
MAX = 1123456

total_c = [0] * MAX
ans = 0

max_pos = 0
for _ in range(c):
    pos = int(input())
    total_c[pos] = -1
    if pos > max_pos: max_pos = pos

max_pos += 1
for _ in range(t):
    x, y = map(int, input().split())
    dist = int(math.ceil(math.sqrt(x**2 + y**2)))
    ans += total_c[dist:max_pos].count(-1)
print(ans)