count = 0
while True:
    c, e, l, p = list(map(int, input().split()))
    if not c: break

    count += 1

    adj = {}
    for i in range(1, c+1):
        adj[i] = []

    for _ in range(e):
        u, v = list(map(int, input().split()))
        adj[u].append(v)
        adj[v].append(u)

    q = []
    visited = [False] * (c+1)
    visited[l] = True
    q.append(l)

    c_pos = []
    layer = [0] * (c+1)

    while q:
        curr = q.pop(0)
        for neighbour in adj[curr]:
            if not visited[neighbour]:
                q.append(neighbour)
                visited[neighbour] = True
                layer[neighbour] = layer[curr] + 1
                if layer[neighbour] <= p:
                    c_pos.append(neighbour)

    print('Teste', count)
    str_c = ''
    for i in sorted(c_pos):
        print(i, end=" ")
    print("\n")
