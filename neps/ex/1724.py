s = int(input())
a = int(input())
b = int(input()) + 1

ans = 0

for i in range(a, b):
    sum = 0
    while i != 0:
        sum += i % 10
        i = i // 10

    if sum == s:
        ans += 1

print(ans)