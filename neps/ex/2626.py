class Graph:
    def __init__(self, n):
        self.n = n

        self.edges = []
        self.times_visited = [0] * self.n
        self.weight = [0] * self.n

        for _ in range(self.n):
            self.edges.append([])

    def add_edges(self, u, v):
        self.edges[u].append(v)
        self.edges[v].append(u)

    def set_weight(self, j, w):
        self.weight[j] = w

    def bfs(self, s, min, max):
        visited = [False] * self.n

        q = []
        q.append(s)

        while q:
            cur = q.pop(0)


            if not visited[cur]:
                self.times_visited[cur] += 1
                visited[cur] = True
                for i in self.edges[cur]:

                    neighbour = i

                    if not visited[neighbour]:
                        if min <= self.weight[neighbour] <= max:
                            q.append(neighbour)


n, m = map(int, input().split())
graph = Graph(n)

for i in range(n):
    w, v = map(int, input().split())
    v -= 1
    graph.add_edges(v, i)
    graph.set_weight(i, w)

for i in range(m):
    anf, min, max = map(int, input().split())
    anf -= 1
    graph.bfs(anf, min, max)

print(*graph.times_visited)
