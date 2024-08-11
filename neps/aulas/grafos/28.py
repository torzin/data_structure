from queue import PriorityQueue
import math


class Graph:
    def __init__(self, n):
        self.n = n
        self.adj = []

        for _ in range(n):
            self.adj.append([])

    def add_edge(self, u, v, w):
        self.adj[u].append([v, w])
        self.adj[v].append([u, w])

    def dijkstra(self, s):
        mark = [False] * self.n
        dist = [math.inf] * self.n

        pq = PriorityQueue()

        dist[s] = 0
        pq.put([0, s])

        for k in range(self.n):

            while True:
                curr = pq.get()[1]

                if not mark[curr]:
                    break

            mark[curr] = True

            for i in range(len(self.adj[curr])):
                neighbour = self.adj[curr][i][0]
                w = self.adj[curr][i][1]

                if dist[neighbour] > dist[curr] + w:
                    dist[neighbour] = dist[curr] + w
                    pq.put([dist[neighbour], neighbour])

        return dist


n, m = map(int, input().split())

graph = Graph(n)

for i in range(m):
    u, v, w = map(int, input().split())
    graph.add_edge(u-1, v-1, w)

ans = graph.dijkstra(0)[-1]
print(ans)
