from queue import SimpleQueue
import math

class Graph:
    def __init__(self, n, is_undirected=True):
        self.n = n
        self.is_undirected = is_undirected

        self.adj = []
        for _ in range(n):
            self.adj.append([])

    def add_edge(self, u, v):
        self.adj[u].append(v)
        if self.is_undirected:
            self.adj[v].append(u)

    def topological_sort(self):

        sorting = []
        q = SimpleQueue()

        in_degree = [0] * self.n

        for i in range(self.n):
            for j in range(len(self.adj[i])):
                in_degree[self.adj[i][j]] += 1

        for i in range(self.n):
            if in_degree[i] == 0:
                q.put(i)

        while not q.empty():
            current = q.get()

            sorting.append(current)

            for i in range(len(self.adj[current])):
                neighbour = self.adj[current][i]

                in_degree[neighbour] -= 1

                if in_degree[neighbour] == 0:
                    q.put(neighbour)

        return sorting


n, m = map(int, input().split())

graph = Graph(n, is_undirected=False)

in_degree = [0] * n
adj = []
for _ in range(n):
    adj.append([])


for i in range(m):
    u, v = map(int, input().split())

    graph.add_edge(u, v)

print("Ordenação topológica: ", end="")

sorting = graph.topological_sort()

print(*sorting)

