n = int(input())
adj = []

for i in range(1, int(n**0.5)+1):

    if n % i == 0:
        adj.append(i)

        if n//i != i:
            adj.append(n//i)

for i in sorted(adj):
    print(i, end=" ")