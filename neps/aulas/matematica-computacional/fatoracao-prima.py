n = int(input())

value = n
primes = [] # Inicialize uma lista vazia para armazenar os fatores primos

# Itere sobre o intervalo de 2 até a raiz quadrada de n
for i in range(2, int(n**0.5) + 1):
    # Enquanto o número atual divide value uniformemente, é um fator primo
    while value%i == 0:
        primes.append(i) # Adicione o fator primo à lista
        value = value//i # Divida value pelo fator primo

# Se houver um primo restante em value, adicione-o à lista
if value != 1:
    primes.append(value)

# Imprima o número de fatores primos
print(f"{len(primes)}")

# Imprima os fatores primos em ordem não decrescente
print(f"{primes[0]}", end="")
for i in range(1, len(primes)):
    print(f" {primes[i]}", end="")

