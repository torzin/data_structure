# Para finalizar nosso curso, iremos aprender uma estrutura de dados mais complexa. Nesta aula aprenderemos a resolver o
# seguinte problema:
# Inicialmente, existem N conjuntos e o i-ésimo conjunto contém apenas o número inteiro i. São dadas algumas perguntas
# de dois tipos:
# Primeiro tipo: dado a e b, se else não pertencerem ao mesmo conjunto, funda os conjuntos desses dois em um
# Segundo tipo: dado a e b, verifique se a e b estão no mesmo conjunto

MAX = 1000010

parent = [0] * MAX
size = [0] * MAX


def find(value):
    if parent[value] == value:
        return value
    parent[value] = find(parent[value])
    return parent[value]


def merge(i, j):
    i = find(i)
    j = find(j)

    if i == j:
        return

    if size[i] >= size[j]:
        parent[j] = i
        size[i] += size[j]
    else:
        parent[i] = j
        size[j] += size[i]


n, q = map(int, input().split())

for i in range(n):
    size[i] = 1
    parent[i] = i

for i in range(q):
    qtype, a, b = map(int, input().split())

    if qtype == 1:
        merge(a, b)
    else:
        if find(a) == find(b):
            print('Mesmo conjunto')
        else:
            print('Conjuntos diferentes')



