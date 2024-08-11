count = 1
while True:
    n = int(input())
    if not n:
        break

    names = input().split()
    dict_names = {}
    adj = []
    for i in range(n):
        dict_names[names[i]] = i
        adj.append([])

    for i in range(n):
        edge = input().split()
        u = dict_names[edge[0]]
        if edge[1] == '0':
            continue
        w = int(edge[1]) + 1
        for j in edge[w:]:
            v = dict_names[j]
            adj[u].append(v)

    q = []
    sorting = []
    in_degree = [0] * n

    for i in range(n):
        for j in range(len(adj[i])):
            in_degree[adj[i][j]] += 1

    for i in range(n):
        if in_degree[i] == 0:
            q.append(i)

    while q:
        current = q.pop(0)

        sorting.append(current)

        for i in range(len(adj[current])):
            neighbour = adj[current][i]

            in_degree[neighbour] -= 1

            if in_degree[neighbour] == 0:
                q.append(neighbour)

    print(f"Teste {count}")
    if not sorting:
        print('impossivel')
    else:
        for i in sorting:
            print(names[i], end=" ")
        print('\n')
    count += 1
