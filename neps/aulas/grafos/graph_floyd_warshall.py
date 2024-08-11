import math

# Lê a quantidade de vértices e a quantidade de arestas
n, m = map(int, input().split())

dp = []

# Criando uma matriz com três dimensões. Como os vértices são 1-indexados, a matriz precisa ter tamanho n + 1
for i in range(
    n + 1
):  # dp[i][j][k] = menor caminho do vértice i para o vértice j de modo a que só possamos utilizar os vértices 1,2,...,k como vértices intermédios
    dp.append([])
    for j in range(n + 1):
        dp[i].append([0] * (n + 1))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            dp[i][j][0] = 0  # Primeiro caso base
        else:
            dp[i][j][0] = math.inf  # Terceiro caso base


for i in range(m):
    # Lê a descrição de uma aresta
    u, v, w = map(int, input().split())

    dp[u][v][0] = w  # Segundo caso base

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dp[i][j][k] = min(dp[i][j][k - 1], dp[i][k][k - 1] + dp[k][j][k - 1])


for i in range(1, n + 1):
    for j in range(1, n + 1):
        if dp[i][j][n] == math.inf:
            print(f"Não há nenhum caminho de {i} para {j}")
        else:
            print(f"O caminho mínimo de {i} para {j} é {dp[i][j][n]}")

print(dp)