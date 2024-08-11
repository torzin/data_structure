n, m = map(int, input().split())

parent = [0] * (n + 1)
size = [0] * (n + 1)

for k in range(1, n + 1):
    parent[k] = k
    size[k] = 1


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


for _ in range(m):
    u, v = map(int, input().split())
    merge(u, v)

ans = 0
visited = []
for i in range(1, n+1):
    curr_parent = find(i)
    if curr_parent in visited:
        continue
    else:
        ans += 1
        visited.append(curr_parent)

print(ans)
