def gcd_extended(a, b):
    if a == 0:
        return 0, 1, b

    x1, y1, gcd = gcd_extended(b%a, b)

    x = y1 - (b//a)*x1
    y = x1

    return x, y, gcd


a, m = map(int, input().split())
inv, y, gcd = gcd_extended(a, m)  # Acha uma solução para a equação ax + my = 1

print(f"Inverso modular de {a} modulo {m} = {inv%m}")


# encontrando o inverso modular para cada número
a, m = map(int, input().split())

inv = [0]*m  # inv[i] = inverso modular de i
inv[1] = 1  # Primeiro caso

for i in range(2, m):
    inv[i] = -(m//i)*(inv[m % i])
    inv[i] = inv[i] % m

print(f"Inverso modular de {a} modulo {m} = {inv[a]}")
