import math

a = int(input())
b = int(input())

cnt = 0

for i in range(a-1, b+1):
    cbrt = math.cbrt(i)
    sqrt = math.sqrt(i)

    if cbrt == int(cbrt) and sqrt == int(sqrt):
        cnt += 1

print(cnt)
