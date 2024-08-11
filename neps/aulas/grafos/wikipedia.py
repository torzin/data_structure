from queue import SimpleQueue

n = int(input())
set_words = set()
adj = {}

for i in range(n):
    u, v = input().split()
    try:
        adj[u].append(v)
    except KeyError:
        adj[u] = []
        adj[u].append(v)
    set_words.add(u)
    set_words.add(v)

set_words = sorted(list(set_words))

for i in range(len(set_words)-1):
    try:
        adj[set_words[i]].append(set_words[i + 1])
    except KeyError:
        adj[set_words[i]] = []
        adj[set_words[i]].append(set_words[i + 1])

    try:
        adj[set_words[i+1]].append(set_words[i])
    except KeyError:
        adj[set_words[i + 1]] = []
        adj[set_words[i + 1]].append(set_words[i])

blankline = input()
A, B = input().split()

q = SimpleQueue()
visited = []
layer = {A: 0}
q.put(A)
visited.append(A)

while not q.empty():
    curr = q.get()

    for neighbour in adj[curr]:
        if neighbour not in visited:
            q.put(neighbour)
            visited.append(neighbour)
            layer[neighbour] = layer[curr] + 1

ans = layer[B]


print(ans)

