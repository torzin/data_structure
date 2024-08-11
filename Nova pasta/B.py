n, m = map(int, input().split())
x, y = map(int, input().split())
x -= 1
y -= 1

visited = [[False] * m for _ in range(n)]
mat = [list(input()) for _ in range(n)]
X = list(input())


def is_possible(i, j):
    if i < 0 or i >= n or j < 0 or j >= m:
        return False
    if mat[i][j] == '#':
        return False
    return True


ax = x
ay = y

for i in X:

    if i == "U":
        if is_possible(ax - 1, ay):
            ax = ax - 1

    elif i == "L":
        if is_possible(ax, ay - 1):
            ay = ay - 1

    elif i == 'R':
        if is_possible(ax, ay + 1):
            ay += 1

    elif i == 'D':
        if is_possible(ax + 1, ay):
            ax += 1

ax += 1
ay += 1
print(ax, ay)