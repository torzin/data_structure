


class Graph:
    def __init__(self, n, is_undirected=True):

        self.n = n
        self.is_undirected = is_undirected

        # Cria a lista de adjacencias
        self.adj = []
        for _ in range(n + 1):
            self.adj.append([])

    def add_edge(self, u, v):
        self.adj[u].append(v)
        if self.is_undirected:  # Caso o grafo seja não direcionado
            self.adj[v].append(u)  # Adicionamos a aresta de v para u

    def count_components(self):
        self.visited = [False] * self.n

        qtdComponents = 0

        for i in range(self.n):
            if not self.visited[i]:
                self.dfs(i)
                qtdComponents += 1

        return qtdComponents

    def dfs(self, current):
        self.visited[current] = True

        for i in range(len(self.adj[current])):
            neighbour = self.adj[current][i]

            if not self.visited[neighbour]:
                self.dfs(neighbour)


n, m = map(int, input().split())
graph = Graph(n)

for i in range(m):
    # Lê a descrição de uma aresta
    u, v = map(int, input().split())

    graph.add_edge(u, v)

print(f"Número de componentes: {graph.count_components()}")
