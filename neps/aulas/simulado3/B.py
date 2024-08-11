n = int(input())

parent = [0] * (n+1)
value = [0] * (n+1)
ins = [False] * (n + 1)
max_val = [0] * (n + 1)

for i in range(1, n+1):
    par, val = map(int, input().split())
    value[i] = val
    parent[i] = par

    if value[i] > value[parent[i]]:

        if value[i] > max_val[parent[i]]:
            max_val[parent[i]] = value[i]

        ins[parent[i]] = True

print(ins.count(True))

for i in range(int(input())):

    idx, v = map(int, input().split())
    value[idx] = v

    if ins[parent[idx]]:
        if value[parent[idx]] >= value[idx]:
            ins[parent[idx]] = False
    else:
        if value[parent[idx]] < value[idx]:
            ins[parent[idx]] = True

    if value[idx] < max_val[idx]:
        ins[idx] = True
    elif value[idx] >= max_val[idx]:
        ins[idx] = False

    print(ins.count(True))
