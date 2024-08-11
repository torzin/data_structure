from queue import PriorityQueue

n = int(input())
ans = 0
max_ans = 0

pq = PriorityQueue()


for _ in range(n):
    en, ex = map(int, input().split())

    pq.put([en, 1])
    pq.put([ex, 0])


while not pq.empty():
    i = pq.get()

    if i[1] == 1:
        ans += 20
    else:
        ans -= 20

    max_ans = max(max_ans, ans)

print(max_ans)
