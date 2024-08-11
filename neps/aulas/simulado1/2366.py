n, m, p = map(int, input().split())

matrix = [list(map(int, input().split())) for i in range(n)]

enzo = 0
lobo = 0


def find_sum(line):
    sum = 0
    for i in range(len(line)):
        sum += line[i]
        line[i] = 0
    return [sum, line]


def get_sum(mat, line, col):

    ans, new_line = find_sum(mat[line])
    mat[line] = new_line
    for i in range(n):
        ans += mat[i][col]
        mat[i][col] = 0

    return [mat, ans]


for i in range(1, p+1):
    l, c = map(int, input().split())
    l -= 1
    c -= 1
    if i % 2 == 0:
        matrix, soma = get_sum(matrix, l, c)
        lobo += soma
    else:
        matrix, soma = get_sum(matrix, l, c)
        enzo += soma

if enzo == lobo:
    print('Empate')
elif enzo > lobo:
    print('Enzo')
else:
    print('Lobo')

