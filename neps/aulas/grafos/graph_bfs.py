from queue import SimpleQueue


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
            self.adj[v].append(u)  # Nós adicionamos a aresta de v para u

    def count_components(self):

        self.visited = [
            False
        ] * self.n  # Cria um vetor que indica se um vértice foi visitado ou não

        qtdComponents = 0  # Guarda a quantidade de componentes do nosso grafo

        for i in range(self.n):
            if not self.visited[i]:
                self.bfs(i)  # Marca todos os vértices que estão na mesma componente do i-ésimo vértice
                qtdComponents += 1

        return qtdComponents

    def bfs(self, source):
        q = SimpleQueue()
        q.put(source)
        self.visited[source] = True

        while not q.empty():
            current = q.get()

            for i in range(len(self.adj[current])):
                neighbour = self.adj[current][i]

                if self.visited[neighbour]:
                    continue

                q.put(neighbour)
                self.visited[neighbour] = True


    # Find the shortest path between A and B:
    # def get_shortest_path(self, A, B):
    #     self.layer = [0] * n
    #
    #     self.visited = [False] * self.n
    #
    #     self.bfs(A)
    #     return self.layer[B]
    #
    # def bfs(self, source):
    #     q = SimpleQueue()
    #     q.put(source)
    #     self.visited[source] = True
    #     self.layer[source] = 0  # A fonte tem camada 0
    #
    #     while not q.empty():
    #         current = q.get()
    #
    #         for i in range(len(self.adj[current])):
    #             neighbour = self.adj[current][i]
    #
    #             if self.visited[neighbour]:
    #                 continue
    #
    #             q.put(neighbour)
    #             self.visited[neighbour] = True
    #             self.layer[neighbour] = (self.layer[current] + 1)  # Atualiza a camada do vértice neighbour


# Lê a número de vértices e o número de arestas
n, m = map(int, input().split())
graph = Graph(n)

for i in range(m):
    # Lê a descrição de uma aresta
    u, v = map(int, input().split())

    graph.add_edge(u, v)

print(f"Número de componentes: {graph.count_components()}")
