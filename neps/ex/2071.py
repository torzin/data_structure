l = int(input())
r = int(input())
s = int(input())

ans = -1

for i in range(r, l+1, -1):
    soma = 0
    lista = list(str(i))
    for j in lista:
        soma += int(j)

    if soma == s:
        ans = i
        break

print(ans)
