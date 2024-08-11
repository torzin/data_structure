n, k = map(int, input().split())

adj = []
nums = sorted(map(int, input().split()))

for i in range(1, k+1):
    adj.append([nums[-1]])
    nums.pop(-1)

nums = nums[::-1]

before = -2
aft = 0
for i in range(k):
    before += 2
    aft += 2
    adj[i] += nums[before:aft]


ans = 0
for k in adj:
    if len(k) < 3:
        continue

    ans += (k[1] - k[2])**2

print(ans)
