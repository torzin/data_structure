from queue import PriorityQueue

n, m = map(int, input().split())
adj = []

in_degree = [0] * n

for _ in range(n):
    adj.append([])

for i in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)

    in_degree[v] += 1

q = PriorityQueue()
sorting = []

for i in range(n):
    if in_degree[i] == 0:
        q.put(i)


while not q.empty():
    current = q.get()

    sorting.append(current)

    for i in range(len(adj[current])):
        neigh = adj[current][i]

        in_degree[neigh] -= 1

        if in_degree[neigh] == 0:
            q.put(neigh)

if len(sorting) != n:
    print("*")
else:
    for i in sorting:
        print(i)
