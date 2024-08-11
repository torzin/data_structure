import math
from queue import PriorityQueue


class Graph:
    def __init__(self, n, types_price):
        self.n = n
        self.types_price = types_price

        self.last_type = -1

        self.adj = []

        for _ in range(n):
            self.adj.append([])

    def add_edge(self, u, v, t):
        self.adj[u].append([v, t])
        self.adj[v].append([u, t])

    def dijkstra(self, s):
        dist = [math.inf] * self.n
        visited = [False] * self.n

        pq = PriorityQueue()
        dist[s] = 0
        pq.put([0, s, -1])

        for k in range(self.n):

            while not pq.empty():
                _, curr, tp = pq.get()

                if not visited[curr]:
                    break

            visited[curr] = True

            if curr == s:
                pass
            else:
                self.last_type = tp

            for j in range(len(self.adj[curr])):

                neighbour = self.adj[curr][j][0]
                type = self.adj[curr][j][1]

                if self.last_type == type:
                    if dist[neighbour] > dist[curr]:
                        dist[neighbour] = dist[curr]
                        pq.put([dist[neighbour], neighbour, type])

                else:
                    if dist[neighbour] > dist[curr] + self.types_price[type]:
                        dist[neighbour] = dist[curr] + self.types_price[type]
                        pq.put([dist[neighbour], neighbour, type])

        return dist


n, m, k = map(int, input().split())
prices = list(map(int, input().split()))

graph = Graph(n, prices)

for i in range(m):
    u, v, m = map(int, input().split())
    graph.add_edge(u-1, v-1, m-1)

a, b = map(int, input().split())
dists = graph.dijkstra(a-1)
if dists[b-1] == math.inf:
    print(-1)
else:
    print(dists[b-1])
