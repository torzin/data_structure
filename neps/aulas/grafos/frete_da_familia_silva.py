class Edges:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w

    def __lt__(self, e):  # Operador será usado pela função sort
        return self.w < e.w


MAX = 1010
parent = [0] * MAX
size = [0] * MAX


def find(value):
    if parent[value] == value:
        return value
    parent[value] = find(parent[value])
    return parent[value]


def merge(i, j):
    i = find(i)
    j = find(j)

    if i == j:
        return

    if size[i] >= size[j]:
        parent[j] = i
        size[i] += size[j]
    else:
        parent[i] = j
        size[j] += size[i]


def init_dsu(n):
    for i in range(n):
        parent[i] = i
        size[i] = 1


class Graph:
    def __init__(self, n, is_undirected=True):
        self.n = n
        self.is_undirected = is_undirected

        self.edges = []

    def add_edge(self, u, v, w):
        self.edges.append(Edges(u, v, w))
        if self.is_undirected:
            self.edges.append(Edges(v, u, w))

    def kruskal(self):
        self.edges.sort()  # ordena pelo peso
        init_dsu(self.n)

        mst_count = 0

        for i in range(len(self.edges)):
            u = self.edges[i].u
            v = self.edges[i].v

            if find(u) != find(v):
                merge(u, v)
                mst_count += self.edges[i].w

        return mst_count


n, m = map(int, input().split())

graph = Graph(n)

for i in range(m):
    u, v, w = map(int, input().split())
    graph.add_edge(u, v, w)

ans = graph.kruskal()
print(ans)
