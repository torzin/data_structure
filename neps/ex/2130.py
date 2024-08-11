class Graph:
    def __init__(self, n, k, m):
        self.n = n
        self.k = k
        self.m = m
        self.mat = [[0] * n for _ in range(m)]
        self.visited = [[False] * n for _ in range(m)]

    def set_cam(self, c, l, pos):
        if pos == "N":
            for i in range(l+1):
                self.mat[i][c] = -1

        if pos == "S":
            for i in range(l, self.m):
                self.mat[i][c] = -1

        if pos == "O":
            for i in range(c+1):
                self.mat[l][i] = -1

        if pos == "L":
            for i in range(c, self.n):
                self.mat[l][i] = -1

    def is_possible(self, x, y):
        if x < 0 or x >= self.m:
            return False

        if y < 0 or y >= self.n:
            return False

        if self.visited[x][y]:
            return False

        if self.mat[x][y] == -1:
            return False

        return True

    def bfs(self):
        q = []

        q.append([0, 0])

        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        if self.mat[0][0] == -1:
            return False

        while q:
            curr_x, curr_y = q.pop(0)

            if not self.visited[curr_x][curr_y]:
                self.visited[curr_x][curr_y] = True

                for i in range(4):
                    new_x = curr_x + dx[i]
                    new_y = curr_y + dy[i]

                    if self.is_possible(new_x, new_y):
                        q.append([new_x, new_y])


        print(self.visited)
        print(self.mat)
        print(self.m, self.n)
        if self.visited[self.m - 1][self.n - 1]:
            return True
        return False


n, m, k = map(int, input().split())

graph = Graph(n, k, m)

for i in range(k):
    c, l, pos = input().split()
    c = int(c) - 1
    l = int(l) - 1

    graph.set_cam(c, l, pos)

if graph.bfs():
    print('S')
else:
    print('N')