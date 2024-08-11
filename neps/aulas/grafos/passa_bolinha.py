n = int(input())
y, x = list(map(int, input().split()))
y -= 1
x -= 1
matrix = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * (n+1) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def is_possible(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if visited[y][x]:
        return False
    return True


def dfs(visited, x, y):
    visited[y][x] = True

    for d in range(4):
        neighbour_x = x + dx[d]
        neighbour_y = y + dy[d]

        if is_possible(neighbour_x, neighbour_y) and matrix[neighbour_y][neighbour_x] >= matrix[y][x]:
            visited[neighbour_y][neighbour_x] = True
            dfs(visited, neighbour_x, neighbour_y)


dfs(visited, x, y)

ans = 0
for i in visited:
    ans += i.count(True)

print(ans)
