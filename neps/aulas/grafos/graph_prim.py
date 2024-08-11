from queue import PriorityQueue
import math

class Graph:
    def __init__(self, n, is_undirected=True):

        self.n = n
        self.is_undirected = is_undirected

        self.adj = []
        for _ in range(n):
            self.adj.append([])

    def add_edge(self, u, v, w):
        self.adj[u].append([v, w])
        if self.is_undirected:
            self.adj[v].append([u, w])

    def prim(self):
        value = [math.inf] * self.n
        mark = [False] * self.n

        mst_cost = 0
        pq = PriorityQueue()

        value[0] = 0
        pq.put([0, 0])

        for k in range(self.n):

            while pq:
                current = pq.get()[1]

                if not mark[current]:
                    break

            mark[current] = True
            mst_cost += value[current]

            for j in range(len(self.adj[current])):
                viz = self.adj[current][j][0]
                w = self.adj[current][j][1]

                if value[viz] > w:
                    value[viz] = w
                    pq.put([value[viz], viz])

        return mst_cost


n, m = map(int, input().split())

graph = Graph(n)

for i in range(m):
    u, v, w = map(int, input().split())
    graph.add_edge(u, v, w)

mst_cost = graph.prim()

print(f"MST tem custo {mst_cost}")

