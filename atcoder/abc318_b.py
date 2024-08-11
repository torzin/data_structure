n = int(input())

MAX = 112
diff = [[0] * MAX for i in range(MAX)]
grid = [[0] * MAX for i in range(MAX)]
dcol = [0] * MAX


while n:

    n -= 1
    diff.append([])
    a, b, c, d = list(map(int, input().split()))

    x1 = a
    y1 = c
    x2 = b - 1
    y2 = d - 1

    diff[x1][y1] += 1
    diff[x1][y2+1] -= 1
    diff[x2 + 1][y1] -= 1
    diff[x2 + 1][y2 + 1] += 1

ans = 0

for i in range(112):
    delta = 0
    for j in range(112):
        dcol[j] += diff[i][j]
        delta += dcol[j]
        grid[i][j] += delta
        if grid[i][j] > 0:
            ans += 1

print(ans)
