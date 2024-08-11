# dados N, K e M a saída tem que ser (N K) mod m:

# Usando triângulo de pascal
n, k, m = map(int, input().split())

if n < k:
    print(f"{n} escolhe {k} é igual a 0")
else:
    triangle = [[0] * (n + 1)]  # triangle[i][j] = i escolhe j módulo m
    triangle[0][0] = 1  # Caso base

    for i in range(1, n + 1):
        triangle.append([0] * (n + 1))

        for j in range(i + 1):
            # Calculando triangle[i][j]
            triangle[i][j] = triangle[i - 1][j]

            if j - 1 >= 0:
                triangle[i][j] = (triangle[i][j] + triangle[i - 1][j - 1]) % m

    print(f"{n} escolhe {k} é igual a {triangle[n][k]}")

# Usando inverso modular
n, k, m = map(int, input().split())

if n < k:
    print(f"{n} escolhe {k} é igual a 0")
else:
    inv = [0] * (n + 1)
    factorial = [0] * (n + 1)
    invFactorial = [0] * (n + 1)

    # Casos base
    inv[1], invFactorial[1] = 1, 1
    factorial[0], factorial[1] = 1, 1

    for i in range(2, n + 1):
        # Calculando factorial[i]
        factorial[i] = (factorial[i - 1] * i) % m

        # Calculando inv[i]
        inv[i] = -(m // i) * (inv[m % i])
        inv[i] = inv[i] % m

        # Calculando invFactorial[i]
        invFactorial[i] = (invFactorial[i - 1] * inv[i]) % m

    ans = factorial[n] * invFactorial[k] * invFactorial[n - k]
    ans = ans % m

    print(f"{n} escolhe {k} é igual a {ans}")
