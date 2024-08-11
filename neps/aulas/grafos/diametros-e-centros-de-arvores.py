import math


class Graph:
    def __init__(self, n, is_undirected=True):

        self.n = n
        self.is_undirected = is_undirected

        # Cria as listas de adjacências
        self.adj = []
        for _ in range(n):
            self.adj.append([])

    def add_edge(self, u, v):
        self.adj[u].append(v)
        if self.is_undirected:  # Se o grafo não for direcionado
            self.adj[v].append(u)  # Nós adicionamos as arestas de v para u

    def get_diameter(self):
        A = self.get_farthest(0)
        B = self.get_farthest(A)

        return self.dist[B]

    def get_centers(self):
        A = self.get_farthest(0)
        B = self.get_farthest(A)

        k = self.dist[B]

        path = []

        while A != B:
            path.append(B)
            B = self.parent[B]

        path.append(A)

        centers = []

        if not k % 2:
            centers.append(path[k // 2])
        else:
            centers.append(path[k // 2])
            centers.append(path[(k+1) // 2])

        return centers

    def get_farthest(self, node):
        self.dist = [math.inf] * self.n
        self.visited = [False] * self.n
        self.parent = [-1] * self.n

        self.dist[node] = 0
        self.dfs(node)

        max_dist = -1
        farthest_node = 0

        for i in range(self.n):
            if max_dist < self.dist[i]:
                farthest_node = i
                max_dist = self.dist[i]

        return farthest_node

    def dfs(self, current):
        self.visited[current] = True

        for i in range(len(self.adj[current])):
            neighbour = self.adj[current][i]

            if not self.visited[neighbour]:

                self.parent[neighbour] = current
                self.dist[neighbour] = self.dist[current] + 1
                self.dfs(neighbour)


n = int(input())

graph = Graph(n)

for i in range(n - 1):
    u, v = map(int, input().split())
    graph.add_edge(u, v)

# diameter = graph.get_diameter()
centers = graph.get_centers()


print(f"Número de centros: {len(centers)}")
print("Centros: ", end="")
print(*centers)
