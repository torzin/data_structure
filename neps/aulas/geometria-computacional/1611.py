import math

n = int(input())

dists = []
for _ in range(n):
    dists.append(list(map(int, input().split())))

dist = sorted(dists, key=lambda x: math)