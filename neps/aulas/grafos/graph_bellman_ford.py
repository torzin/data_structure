import math


class Edges:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w


class Graph:
    def __init__(self, n, is_undirected=True):
        self.n = n
        self.is_undirected = is_undirected

        self.edges = []

    def add_edge(self, u, v, w):
        edge = Edges(u, v, w)
        self.edges.append(edge)
        if self.is_undirected:
            edge = Edges(v, u, w)
            self.edges.append(edge)

    def bellman_ford(self, s):
        dist = [math.inf] * self.n
        dist[s] = 0

        for step in range(self.n-1):
            for i in range(len(self.edges)):
                u = self.edges[i].u
                v = self.edges[i].v

                if dist[u] != math.inf:
                    dist[v] = min(dist[v], dist[u] + self.edges[i].w)

        for i in range(len(self.edges)):
            u = self.edges[i].u
            v = self.edges[i].v

            if dist[v] > dist[u] + self.edges[i].w:
                return []
        return dist


n, m, s = map(int, input().split())

graph = Graph(n)

for i in range(m):
    u, v, w = map(int, input().split())
    graph.add_edge(u, v, w)

dist = graph.bellman_ford(s)

if len(dist) == 0:
    print("O grafo tem um ciclo de peso negativo")
else:
    for i in range(n):
        print(f"A distância entre {s} e {i} é {dist[i]}")
