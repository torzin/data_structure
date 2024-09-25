from queue import PriorityQueue
import math

n, m, k = map(int, input().split())

transport = {}
t_inp = list(map(int, input().split()))

for idx, number in enumerate(t_inp):
    transport[idx+1] = number

adj = [[] for i in range(n+1)]

for _ in range(m):
    a, b, t = map(int, input().split())
    adj[a].append([b, t])
    adj[b].append([a, t])

a, b = map(int, input().split())


def dijkstra(s):
    pq = PriorityQueue()
    dists = [math.inf] * (n + 1)
    visited = [False] * (n + 1)

    dists[a] = 0
    pq.put((0, s, -1))

    while not pq.empty():
        current_cost, current, tp = pq.get()

        if visited[current]:
            continue

        visited[current] = True

        for neighbour, system in adj[current]:
            travel_cost = transport[system] if tp != system else 0

            new_cost = current_cost + travel_cost

            if new_cost < dists[neighbour]:
                dists[neighbour] = new_cost
                pq.put((new_cost, neighbour, system))

    return dists


ans = dijkstra(a)[b]

if ans == math.inf:
    print(-1)
else:
    print(ans)
