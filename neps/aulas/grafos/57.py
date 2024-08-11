import sys
sys.setrecursionlimit(10**8)

n, m = map(int, input().split())
mat = []

ac_x = 0
ac_y = 0

ans_x = 0
ans_y = 0

for i in range(n):
    line = list(map(int, input().split()))
    mat.append(line)

    if 3 in line:
        ans_x = line.index(3)
        ans_y = i


def is_possible(i, j):
    if i < 0 or i >= n or j < 0 or j >= m:
        return False
    return True


dx = [0, 1, 0, -1, -1, 1, 1, -1]
dy = [1, 0, -1, 0, 1, 1, -1, -1]


x = ans_x
y = ans_y

count = 0
flag = 1

found = False

visited = [[False] * m for i in range(n)]
visited[y][x] = True

while not found:

    for i in range(8):

        new_x = ans_x + dx[i]
        new_y = ans_y + dy[i]

        if 0 <= new_x < m:
            if 0 <= new_y < n:
                if mat[new_y][new_x] != 0 and visited[new_y][new_x] == False:
                    flag += 1
                    break

    visited[new_y][new_x] = True
    if mat[new_y][new_x] == 2:
        found = True
    ans_x = new_x
    ans_y = new_y

ans = flag
print(ans)
