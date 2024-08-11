a = int(input())
b = int(input())
c = int(input())

total_viagem = 0
if a < b < c:
    print(1)
elif a + b < c:
    print(1)
elif a == b == c:
    print(3)
else:
    print(2)
