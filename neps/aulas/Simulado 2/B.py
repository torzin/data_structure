import math
from queue import PriorityQueue

import math
from queue import PriorityQueue


class Graph:
    def __init__(self, n, is_undirected=False):

        self.n = n
        self.is_undirected = is_undirected

        # Cria as listas de adjacências
        self.adj = []
        for _ in range(n):
            self.adj.append([])

    def add_edge(self, u, v, w):
        self.adj[u].append([v, w])
        self.adj[v].append([u, w])

    def dijkstra(self, s):
        dist = [
            math.inf
        ] * self.n  # dist[i] = menor caminho entre s e i encontrado até agora
        mark = [False] * self.n
        # mark[i] = true, se e somente se, nós já tivermos achado o menor caminho entre s e i

        pq = PriorityQueue()

        dist[s] = 0
        pq.put([0, s])

        last_w = -1

        for k in range(self.n):

            while pq:  # Acha o vértice desejado
                current = pq.get()[1]  # Pega o topo da nossa priority queue e remove-o

                if not mark[current]:  # Checa se o vértice atual não está marcado
                    break

            mark[current] = True

            for j in range(len(self.adj[current])):

                neighbour = self.adj[current][j][0]
                w = self.adj[current][j][1]

                if last_w != w:
                    last_w = w
                else:
                    w = 0

                if not mark[neighbour]:
                    print(neighbour)
                    if dist[neighbour] > dist[current] + w:
                        dist[neighbour] = dist[current] + w
                        pq.put([dist[neighbour], neighbour])
                    print(dist)

        return dist


n, m, len_k = map(int, input().split())
k = list(map(int, input().split()))

graph = Graph(n, True)
for i in range(m):
    u, v, idx = map(int, input().split())
    graph.add_edge(u-1, v-1, k[idx-1])

a, b = map(int, input().split())
dist = graph.dijkstra(a-1)
ans = dist[b-1]

print(dist)



