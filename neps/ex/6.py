inf = 2000000000001
n = 0
v = []


def inversoes(v):
    s = len(v)
    if s == 1: return 0

    a, b = [], []
    inv = 0

    # divide v em suas duas metades a e b
    for i in range(0, s // 2): a.append(v[i])
    for i in range(s // 2, s): b.append(v[i])

    # calcula a quantidade de inversões em a e b
    # e atualiza a quantidade de inversoes em v
    inv += inversoes(a)
    inv += inversoes(b)

    a.append(inf)
    b.append(inf)

    ai, bi = 0, 0

    for i in range(s):
        if a[ai] <= b[bi]:
            v[i] = a[ai]
            ai += 1

            # se a[ai] é menor que b[bi] então a[ai] configura uma
            # inversão com todo elemento em b a partir de b[bi]
            inv += len(b) - bi - 1
        else:
            v[i] = b[bi]
            bi += 1

    return inv


n = int(input())

# armazena a soma dos quadrados de x e y em v
for i in range(n):
    x, y = [int(x) for x in input().split()]
    v.append(x * x + y * y)

print(inversoes(v))
