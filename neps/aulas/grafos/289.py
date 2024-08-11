n, m = map(int, input().split())

adj = []
for _ in range(n+1):
    adj.append([])


def find_path(req_val, start_val):
    if req_val in adj[start_val]:
        return 1
    return 0


anss = []
for i in range(m):
    t, a, b = map(int, input().split())
    if t:
        adj[a].append(b)
        adj[b].append(a)
    else:
        ans = find_path(a, b)
        anss.append(ans)

for i in anss:
    print(i)
