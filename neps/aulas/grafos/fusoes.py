n, k = map(int, input().split())

parent = [0] * (n+1)
size = [0] * (n+1)


def find(value):
    if parent[value] == value:
        return value
    parent[value] = find(parent[value])
    return parent[value]


def merge(i, j):
    i = find(i)
    j = find(j)

    if size[i] >= size[j]:
        parent[j] = i
        size[i] += size[j]
    else:
        parent[i] = j
        size[j] += size[i]


for i in range(1, n+1):
    size[i] = 1
    parent[i] = i

for i in range(k):
    char, n1, n2 = input().split()
    n1 = int(n1)
    n2 = int(n2)

    if char == 'F':
        merge(n1, n2)
    else:
        if find(n1) == find(n2):
            print('S')
        else:
            print('N')