import math
from queue import PriorityQueue


class Graph:
    def __init__(self, n, m, is_undirected=True):
        self.n = n
        self.m = m
        self.is_undirected = is_undirected

        self.adj = []

        for _ in range(n):
            self.adj.append([])

    def add_edge(self, u, v, w):
        self.adj[u].append([v, w])
        if self.is_undirected:
            self.adj[v].append([u, w])

    def dijkstra(self, s):
        dist = [math.inf] * self.n
        mark = [False] * self.n

        pq = PriorityQueue()
        dist[s] = 0

        pq.put([0, s])

        for k in range(self.n):
            while True:
                current = pq.get()[1]

                if not mark[current]:
                    break

            mark[current] = True

            for j in range(len(self.adj[current])):
                neighbour = self.adj[current][j][0]
                w = self.adj[current][j][1]

                if dist[neighbour] > dist[current] + w:
                    dist[neighbour] = dist[current] + w
                    pq.put([dist[neighbour], neighbour])

        return dist


n, m = list(map(int, input().split()))

graph = Graph(n=n+2, m=m)

for i in range(m):
    try:
        u, v, w = list(map(int, input().split()))
        graph.add_edge(u, v, w)
    except EOFError:
        break

dists = graph.dijkstra(0)
ans = dists[n+1]
print(ans)
