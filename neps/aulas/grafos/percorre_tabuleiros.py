# DFS Approach
n = 0
m = 0


def is_cell_valid(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if board[x][y] == 1:
        return False
    if visited[x][y]:
        return False

    return True


def dfs(x, y):
    visited[x][y] = True

    if is_cell_valid(x + 1, y):  # Checa se podemos ir para o sul
        dfs(x + 1, y)

    if is_cell_valid(x, y + 1):  # Checa se podemos ir para o leste
        dfs(x, y + 1)

    if is_cell_valid(x - 1, y):  # Checa se podemos ir para o norte
        dfs(x - 1, y)

    if is_cell_valid(x, y - 1):  # Checa se podemos ir para o oeste
        dfs(x, y - 1)


n, m = map(int, input().split())

board = []  # board[i][j] = 1, se e somente se a célula (i,j) está quebrada
visited = []


for i in range(n):
    board.append(list(map(int, input().split())))

    # Initialize visited
    for _ in range(n):
        visited.append([0 for _ in range(m)])

qtd_components = 0

for x in range(n):
    for y in range(m):
        if (
            visited[x][y] or board[x][y] == 1
        ):  # Checa se já visitamos essa célula anteriormente ou se ela está quebrada
            continue

        # Nós achamos uma nova componente

        dfs(x, y)  # Marca todas as células da mesma componente da célula (x,y)
        qtd_components += 1  # Aumenta a nossa resposta em 1

print(f"Número de componentes: {qtd_components}")
















# BFS Approach
from queue import SimpleQueue

n = 0
m = 0


def is_cell_valid(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if board[x][y] == 1:
        return False
    if visited[x][y]:
        return False

    return True

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def bfs(x, y):
    q = SimpleQueue()

    visited[x][y] = True
    q.put((x, y))

    while not q.empty():
        currentX, currentY = q.get()

        for d in range(4):
            neighbour_x = dx[d] + currentX
            neighbour_y = dy[d] + currentY

            if is_cell_valid(neighbour_x, neighbour_y):
                visited[neighbour_x][neighbour_y] = True
                q.put((neighbour_x, neighbour_y))


n, m = map(int, input().split())

board = []  # board[i][j] = 1, se e somente se a célula (i,j) está quebrada
visited = []


for i in range(n):
    board.append(list(map(int, input().split())))

    # Initialize visited
    for _ in range(n):
        visited.append([0 for _ in range(m)])

qtd_components = 0

for x in range(n):
    for y in range(m):
        if (
            visited[x][y] or board[x][y] == 1
        ):  # Checa se já visitamos essa célula anteriormente ou se ela está quebrada
            continue

        # Nós achamos uma nova componente

        bfs(x, y)  # Marca todas as células da mesma componente da célula (x,y)
        qtd_components += 1  # Aumenta a nossa resposta em 1

print(f"Número de componentes: {qtd_components}")
