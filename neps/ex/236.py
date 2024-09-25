n = int(input())

sum_col = [0] * n
sum_lin = [0] * n
sum_dig = [0] * 2

mat = []
for _ in range(n):
    line = list(map(int, input().split()))
    mat.append(line)

for i in range(n):
    for j in range(n):
        sum_lin[i] += mat[i][j]
        sum_col[i] += mat[j][i]

        if i == j:
            sum_dig[0] += mat[i][j]

        if i + j == n - 1:
            sum_dig[1] += mat[i][j]

if set(sum_lin) == set(sum_col) == set(sum_dig) and len(set(sum_dig)) == len(set(sum_col)) == len(set(sum_lin)) == 1:
    print(list(sum_col)[0])
else:
    print(-1)