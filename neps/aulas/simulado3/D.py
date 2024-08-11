n = int(input())
i = int(input())
p = int(input())


if p >= n:
    i += p % n
else:
    i += p

if i > n:
    print(i % n)
else:
    print(i)

