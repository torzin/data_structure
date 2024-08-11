n, m = list(map(int, input().split()))

matrix = []
visited = []
layers = []
x, y = 0, 0
for i in range(n):
    visited.append([False] * m)
    layers.append([0] * m)
    line = list(map(int, input().split()))
    if 3 in line:
        y = i
        x = line.index(3)
    matrix.append(line)


def is_possible(x, y):
    if x < 0 or x >= m or y < 0 or y >= n:
        return False
    if visited[y][x]:
        return False
    if matrix[y][x] == 2:
        return False
    return True


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

q = []
q.append((x, y))
visited[y][x] = True
found_x, found_y = 0, 0


while q:
    curr_x, curr_y = q.pop(0)

    if matrix[curr_y][curr_x] == 0:
        found_x = curr_x
        found_y = curr_y
        break

    for d in range(4):
        neighbour_x = dx[d] + curr_x
        neighbour_y = dy[d] + curr_y

        if is_possible(neighbour_x, neighbour_y):
            visited[neighbour_y][neighbour_x] = True
            q.append((neighbour_x, neighbour_y))
            layers[neighbour_y][neighbour_x] = layers[curr_y][curr_x] + 1

print(layers[found_y][found_x])
