n, m, x, y, k = list(map(int, input().split()))

matrix = []
visited = []
for _ in range(n + 1):
    matrix.append([0] * (m + 1))
    visited.append([False] * (m + 1))

for i in range(k):
    u, v = list(map(int, input().split()))
    matrix[u][v] = -1


def is_possible(x, y):
    if x <= 0 or x > n or y <= 0 or y > m:
        return False
    if matrix[x][y] == -1:
        return False
    if visited[x][y]:
        return False
    return True


dy = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
dx = [1, 1, 1, 0, 0, 0, -1, -1, -1]

q = []
q.append((x, y))
visited[x][y] = True
colored = 1

while q:
    curr_x, curr_y = q.pop()

    for i in range(9):
        if dx[i] == 0 and dy[i] == 0:
            continue

        neighbour_x = dx[i] + curr_x
        neighbour_y = dy[i] + curr_y

        if is_possible(neighbour_x, neighbour_y) and visited[neighbour_x][neighbour_y] == False:
            q.append((neighbour_x, neighbour_y))
            colored += 1

            visited[neighbour_x][neighbour_y] = True

print(colored)
