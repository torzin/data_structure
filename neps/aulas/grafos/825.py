n, f = map(int, input().split())

visited = []
mat = []
for _ in range(n):
    visited.append([False] * n)
    mat.append(list(input()))


def is_possible(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if visited[x][y]:
        return False
    if mat[x][y] == "*":
        return False
    if int(mat[x][y]) > f:
        return False

    return True


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

q = []
q.append([0, 0])
visited[0][0] = True

if int(mat[0][0]) > f:
    for i in mat:
        print(''.join(i))
else:
    mat[0][0] = '*'
    while q:
        curr_x, curr_y = q.pop(0)
        for i in range(4):
            new_x = curr_x + dx[i]
            new_y = curr_y + dy[i]

            if is_possible(new_x, new_y):
                visited[new_x][new_y] = True
                mat[new_x][new_y] = '*'
                q.append([new_x, new_y])

    for i in mat:
        print(''.join(i))
