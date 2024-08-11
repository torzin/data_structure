# Encontrando a fatoração prima de um único número inteiro
n = int(input())
spf = []

for i in range(n + 1):
    spf.append(i)

for x in range(2, n + 1):
    if spf[x] != x:
        continue

    for i in range(2 * x, n + 1, x):
        spf[i] = min(spf[i], x)

value = n
primes = []

while value != 1:
    primes.append(spf[value])
    value = value // spf[value]

print(f"Fatoração prima de {n}: {primes[0]}", end="")

for i in range(1, len(primes)):
    print(f"*{primes[i]}", end="")
print('\n')

# Encontrando todos os divisores de um número n
divisors = []

for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
        divisors.append(i)

        if n // i != i:
            divisors.append(n // i)

print(f"Todos os divisores de {n}: ", end="")

for divisor in divisors:
    print(f"{divisor} ", end="")

# Encontrando os divisores de todos os números no intervalo [1,n]
divisors = []
for _ in range(n + 1):
    divisors.append([])

for i in range(1, n + 1):
    for j in range(i, n + 1, i):
        divisors[j].append(i)

for i in range(1, n + 1):
    print(f"Todos os divisores {i}: ", end="")

    for divisor in divisors[i]:
        print(f"{divisor} ", end="")

    print("")

# Número de divisores
value = n
qtd_divisores = 1

for i in range(2, int(n**0.5) + 1):
    exp = 0

    while value % i == 0:
        exp += 1
        value //= i

    qtd_divisores *= exp+1

if value != 1:
    qtd_divisores *= 2

print(f"{n} has {qtd_divisores} divisors")
