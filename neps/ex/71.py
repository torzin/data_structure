V = [2, 5, 10, 20, 50, 100]

memo = [[-1] * 5001 for _ in range(6)]

S = int(input())
N = list(map(int, input().split()))

def dp (i, s):
    if i == 6:
        if s == 0:
            return 1
        else:
            return 0

    if memo[i][s] != -1:
        return memo[i][s]

    memo[i][s] = 0

    for k in range(0, N[i] + 1):
        if s - k * V[i] >= 0:
            memo[i][s] += dp(i + 1, s - k * V[i])

    return memo[i][s]

print(dp(0, S))
