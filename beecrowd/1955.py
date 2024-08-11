n = int(input())
def ns(x):
    if x == '1':
        return 0
    else:
        return 1
mat = [list(map(lambda x: ns(x), input().split())) for i in range(n)]
ans = 1
visited = [0] * n

def dfs(u, c):
    ans = 1
    if visited[u]:
        return visited[u] == c
    visited[u] = c
    for v in range(n):
        if mat[u][v] and v != u:
            ans &= dfs(v, c ^ 3)
    return ans

for u in range(n):
    if visited[u]:
        pass
    else:
        ans &= dfs(u, 1)
if ans:
    print("Bazinga!")
else:
    print('Fail!')