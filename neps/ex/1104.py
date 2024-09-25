n = int(input())

l = [int(input()) for _ in range(n)]
lc = l.copy()
lc.sort(reverse=True)

count = 0
for i in range(1, n+1):
    if lc[i-1] >= i:
        count += 1

print(count)