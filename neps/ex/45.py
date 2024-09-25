n = int(input())

# Leitura da matriz
matrix = [list(map(int, input().split())) for _ in range(n)]

# Pré-calculando as somas de linhas e colunas
row_sums = [sum(matrix[i]) for i in range(n)]
col_sums = [sum(matrix[j][i] for j in range(n)) for i in range(n)]

max_sum = 0

# Iterando sobre a matriz para encontrar o máximo
for i in range(n):
    for j in range(n):
        # Soma da linha i + soma da coluna j - o elemento matrix[i][j] (já que ele aparece duas vezes)
        current_sum = row_sums[i] + col_sums[j] - matrix[i][j] - matrix[i][j]
        max_sum = max(current_sum, max_sum)

print(max_sum)
