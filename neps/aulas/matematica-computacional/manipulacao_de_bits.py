a, b = map(int, input().split())

print(a & b)  # AND bitwise de dois números
print(a | b)  # OR bitwise de dois números
print(a ^ b)  # XOR bitwise de dois números


def left_shift(x, k):
	return x << k


def right_shift(x, k):
	return x >> k


x, k = map(int, input().split())
print(left_shift(x, k), right_shift(x, k))

# NOT bitwise de um número
a = int(input())
print(~a)


# Checar se um bit está ativo
def esta_ativo(x, k):
	return x & (1 << k) != 0


# Acender um bit
def acender_bit(x, k):
	return x | (1 << k)


x, k = map(int, input().split())
x = acender_bit(x, k)


# Apagar um bit
def apagar_bit(x, k):
	return x & ~(1 << k)


x, k = map(int, input().split())
x = apagar_bit(x, k)


# Inverter um bit
def inverter_bit(x, k):
	return x ^ (1 << k)


x, k = map(int, input().split())
x = inverter_bit(x, k)


# Checar se é potencia de dois
def eh_potencia_de_dois(x):
	return x & (x - 1) == 0


# Checar se um conjunto é subconjunto de outro conjunto
def eh_submascara(a, b):
	return a & b == a


# Iterar por todas as submascaras de um número
m = int(input())
s = m

while s > 0:
	s = (s - 1) & m

# Iterar por todas as máscaras e suas submáscaras
n = int(input())

for m in range (1 << n):
	s = m
	while s > 0:
		s = (s - 1) & m



