n, k, m = map(int, input().split())

if n < k:
    print(0)
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

    print(ans)