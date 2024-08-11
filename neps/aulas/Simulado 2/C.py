from queue import PriorityQueue

n, m = map(int, input().split())

carros = sorted(list(map(int, input().split())), reverse=True)

mec = sorted(list(map(int, input().split())))

total_tempo = 0

pq = PriorityQueue()
for i in range(m):
    pq.put((0, i))

for i in carros:
    cur, id = pq.get()

    total_tempo += i * cur

    pq.put((cur + mec[id], id))

print(total_tempo)

