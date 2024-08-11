# uso a bibilioteca sys para limitar o a fila de recursao
from sys import setrecursionlimit

setrecursionlimit(10000)

# leio a entrada
n, m = map(int, input().split())
g = [["" for i in range(m)] for j in range(n)]


# função dfs, que simula o vazamento pela parede
def dfs(i, j):
    # se a posição atual não é uma goteira, paro a dfs
    if g[i][j] != "o":
        return
    # se não há uma linha em baixo de mim, não tem como molhar mas nenhuma posição
    if i + 1 >= n:
        return

    # se a posição em baixo é parede, tranformo ela em goteira "o" e inicio uma nova dfs a partir desse ponto
    if g[i + 1][j] == ".":
        g[i + 1][j] = "o"
        dfs(i + 1, j)
    # caso contrário, se a posição em baixo for prateleira, posso molhar os vizinhos - à esquerda e à direita -  da mesma linha "i"
    # logo, transformo esses pontos em goteira e chamo suas dfs's
    elif g[i + 1][j] == "#":
        if j - 1 >= 0 and g[i][j - 1] == ".":
            g[i][j - 1] = "o"
            dfs(i, j - 1)
        if j + 1 < m and g[i][j + 1] == ".":
            g[i][j + 1] = "o"
            dfs(i, j + 1)
    return


# leio a entrada
for i in range(n):
    linha = input()
    for j in range(m):
        g[i][j] = linha[j]
# encontro o vazamento da primeira linha e inicio a dfs
for j in range(m):
    if g[0][j] == "o":
        dfs(0, j)
# retorno a resposta
for i in range(n):
    for j in range(m):
        print(g[i][j], end="")
    print()
