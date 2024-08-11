# Verificar se os números são primos ou não
q, n = map(int, input().split())

is_prime = [True] * (n + 1)  # is_prime[i] = true se e somente se i for primo

for x in range(2, n+1):  # Itera pelo intervalo [2,n]
    if not is_prime[x]:
        continue

    for i in range(2*x, n+1, x):  # Itera por todo múltiplo de x maior que ele e menor ou igual a n
        is_prime[i] = False


for _ in range(q):
    v = int(input())

    if is_prime[v]:
        print(f'{v} é um número primo')
    else:
        print(f'{v} não é um número primo')


# Encontra o menor fator primo de um número
spf = []  # spf[i] = menor fator primo de i

for i in range(n+1):
    spf.append(i)

for x in range(2, n+1):
    if spf[x] != x:
        continue

    for i in range(2*x, n+1, x):
        spf[i] = min(spf[i], x)

for _ in range(q):
    v = int(input())
    print(f"O menor fator primo de {v} é {spf[v]}")



