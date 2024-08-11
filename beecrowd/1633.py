from heapq import heapify, heappush, heappop

while True:
    try:
        n = int(input())
        t = 1
        ans = 0
        queries = []
        q = []
        heapify(q)
        for i in range(n):
            ct = list(map(int, input().split()))
            ct[0], ct[1] = ct[1], ct[0]
            queries.append(ct)
        queries.sort(key=lambda x: x[1])
        i = 0
        while i < n or q != []:
            while i < n and queries[i][0] <= t:
                heappush(q, queries[i])
                i += 1
            if q:
                ans += t - q[0][0]
                t += q[0][1]
                heappop(q)
            elif i < n:
                t = queries[i][0]

        print(ans)

    except KeyboardInterrupt:
        break
