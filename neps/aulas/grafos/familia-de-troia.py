import sys
sys.setrecursionlimit(10 ** 8)

n, m = input().split()
n, m = int(n), int(m)

adj = {}

for i in range(1, 1+n):
    adj[i] = []

for _ in range(m):
    u, v = input().split()
    u, v = int(u), int(v)

    adj[u].append(v)
    adj[v].append(u)


n_fam = 0
visited = [False] * (n+1)


def dfs(curr, visited):
    visited[curr] = True

    for i in adj[curr]:
        if not visited[i]:
            dfs(i, visited)


for i in range(1, n+1):
    if not visited[i]:
        n_fam += 1
    dfs(i, visited)

print(n_fam)
