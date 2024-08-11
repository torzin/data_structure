import heapq

n, q = map(int, input().split())
a = list(map(int, input().split()))

ans = []

for i in range(q):
    dist = []
    num, idx = map(int, input().split())

    for k in range(n):
        heapq.heappush(dist, abs(num - a[k]))


    ans.append(dist[idx-1])

for i in ans:
    print(i)
