class Graph:
    def __init__(self, n):
        self.n = n
        self.adj = []
        for i in range(0, n + 1):
            self.adj.append([])
        self.weight = [0] * (n + 1)

    def add_edge(self, u, v):
        self.adj[v].append(u)

    def dfs(self, v):
        if len(self.adj[v]) == 0:
            self.weight[v] = 1
            return self.weight[v]
        cnt = int(1)
        for i in self.adj[v]:
            cnt += self.dfs(i)
        self.weight[v] = cnt
        return self.weight[v]

    def isbalanced(self, v):
        if len(self.adj[v]) == 0:
            return True
        current_weight = int(self.weight[self.adj[v][0]])
        for i in self.adj[v]:
            if current_weight != self.weight[i] or self.isbalanced(i) == False:
                return False
        return True


n = int(input())
g = Graph(n)
for i in range(0, n):
    u, v = map(int, input().split())
    g.add_edge(u, v)

g.dfs(0)

if g.isbalanced(0):
    print('bem')
else:
    print('mal')
