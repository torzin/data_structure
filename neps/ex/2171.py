n = int(input())

ts = 0

camels = []

for _ in range(n):
    camel = int(input())
    ts += camel
    camels.append(camel)

median = ts // n

for c in camels:
    print(median - c)
