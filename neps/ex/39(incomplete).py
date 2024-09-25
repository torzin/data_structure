n, k = map(int, input().split())

dp = [[0 for _ in range(k+1)] for i in range(n+1)]

dp[0][0] = 1

for i in range(n):

    for j in range(k):
        dp[i+1][0] += dp[i][j]
        dp[i+1][j+1] += dp[i][j]

print(sum(dp[n]) % (10**9 + 7))
