class Graph:
    def __init__(self, n, weight):

        self.n = n
        self.adj = []

        for _ in range(n):
            self.adj.append([])

        self.weight = [0] + weight

        self.max_count = 0

    def add_edge(self, u, v):
        if self.weight[u] > self.weight[v]:
            self.adj[u].append(v)
        else:
            self.adj[v].append(u)

    def dfs(self, s):
        count = 0
        for i in self.adj[s]:
            count += self.dfs(i)

            if count > self.max_count:
                self.max_count = count

        return count + 1


s, t, p = map(int, input().split())
weight = list(map(int, input().split()))

g = Graph(s+1, weight)

for _ in range(t):
    a, b = map(int, input().split())
    g.add_edge(a, b)

g.dfs(p)

print(g.max_count)


