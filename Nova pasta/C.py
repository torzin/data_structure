n, X, Y = map(int, input().split())
a = map(int, input().split())
b = map(int, input().split())

dishes = sorted(zip(a, b), key=lambda x: (x[0], x[1]), reverse=True)

total_s = 0
total_d = 0
count = 0

for doce, salgado in dishes:

    total_s += salgado
    total_d += doce
    count += 1

    if total_s > Y or total_d > X:
        break


print(count)
