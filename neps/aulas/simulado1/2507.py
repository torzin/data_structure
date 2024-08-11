n = int(input())
ans = 0
max_dec = n
for i in range(1, (n//2)+1):
    ans += abs(i - max_dec)
    max_dec -= 1

ans = ans * 2
print(ans)