n, m = map(int, input().split())

mat = []
start_x = 0
start_y = 0
visited = []
for k in range(n):
    visited.append([False] * m)
    line = input()
    mat.append(line)
    if 'o' in line:
        start_x = line.index('o')
        start_y = k


def is_possible(i, j):

    if i < 0 or i >= n or j < 0 or j >= m:
        return False

    if mat[i][j] != "H":
        return False

    if visited[i][j]:
        return False

    return True


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

cords = []
q = []
q.append([start_y, start_x])
visited[start_y][start_x] = True

while q:
    curr_y, curr_x = q.pop(0)

    for d in range(4):
        new_x = curr_x + dx[d]
        new_y = curr_y + dy[d]

        if is_possible(new_y, new_x):
            visited[new_y][new_x] = True
            q.append([new_y, new_x])
            cords.append([new_y+1, new_x+1])

print(*cords[-1])
