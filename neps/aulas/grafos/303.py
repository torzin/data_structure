import math
from queue import PriorityQueue

class Graph:
    def __init__(self, n, is_undirected=True):
        self.n = n
        self.is_undirected = is_undirected

        self.adj = []
        for _ in range(n):
            self.adj.append([])

    def add_edge(self, u, v, w):
        done = False
        for idx, i in enumerate(self.adj[u]):
            if i[0] == v and i[1] > w:
                self.adj[u].pop(idx)
                self.adj[v].pop(self.adj[v].index([u, i[1]]))

                self.adj[u].append([v, w])
                self.adj[v].append([u, w])

                done = True

        if not done:
            self.adj[u].append([v, w])
            self.adj[v].append([u, w])

    def dijkstra(self, s):
        dist = [math.inf] * self.n
        mark = [False] * self.n

        pq = PriorityQueue()

        dist[s] = 0
        pq.put([0, s])

        for k in range(self.n):

            while True:  # Acha o vértice desejado
                current = pq.get()[1]  # Pega o topo da nossa priority queue e remove-o

                if not mark[current]:  # Checa se o vértice atual não está marcado
                    break

            mark[current] = True

            for j in range(len(self.adj[current])):
                neighbour = self.adj[current][j][0]
                w = self.adj[current][j][1]

                if dist[neighbour] > dist[current] + w:
                    dist[neighbour] = dist[current] + w
                    pq.put([dist[neighbour], neighbour])

        return dist


n, m = map(int, input().split())

graph = Graph(n)

for i in range(m):
    u, v, w = map(int, input().split())
    graph.add_edge(u, v, w)

max_dis = math.inf
for i in range(n):
    ac_dis  = graph.dijkstra(i)
    if max(ac_dis) < max_dis:
        max_dis = max(ac_dis)

print(max_dis)
