import math
from queue import PriorityQueue

class Graph:
    def __init__(self, n, lim):
        self.n = n
        self.lim = lim

        self.adj = []

        for _ in range(n):
            self.adj.append([])

    def add_edge(self, u, v, t, p):
        self.adj[u].append([v, t, p])
        self.adj[v].append([u, t, p])

    def dijkstra(self, s):
        visited = [False] * self.n
        dist = [[math.inf, math.inf] for _ in range(self.n)]

        pq = PriorityQueue()
        pq.put([0, 0, s])

        dist[0] = [0, 0]

        for k in range(self.n):
            while not pq.empty():
                cur = pq.get()[2]

                if not visited[cur]:
                    break

            visited[cur] = True

            for i in range(len(self.adj[cur])):
                neighbour = self.adj[cur][i][0]
                time = self.adj[cur][i][1]
                price = self.adj[cur][i][2]

                if dist[neighbour][0] > dist[cur][0] + time:
                    dist[neighbour][0] = dist[cur][0] + time
                    if dist[cur][1] + price <= self.lim:
                        dist[neighbour][1] = dist[cur][1] + price
                    else:
                        continue

                    pq.put([dist[neighbour][0], dist[neighbour][1], neighbour])

        return dist


lim, n, m = map(int, input().split())

graph = Graph(n=n, lim=lim)

for _ in range(m):
    u, v, t, p = map(int, input().split())

    graph.add_edge(u-1, v-1, t, p)

a, b = map(int, input().split())
ans = graph.dijkstra(a-1)
if ans[b-1][1] <= lim:
    print(ans[b-1][0])
else:
    print(-1)
