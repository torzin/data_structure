n, m = int(input())

parent = [0] * (n + 1)
value = [0] * (n + 1)

for i in range(1, n+1):
    mod, val = map(int, input().split())

    parent[i] = mod
    value[i] = val


times = [0] * n



