def gcd_extended(a, b):
    if a == 0:
        return 0, 1, b  # Base solution for a = 0 is (x,y) = (0,1)

    x1, y1, gcd = gcd_extended(b % a, a)  # Acha o mdc(a,b) e a solução para (b%a,a)

    # Calcula a solução baseada em x1 e y1
    x = y1 - (b // a) * x1
    y = x1

    return x, y, gcd


a, b = map(int, input().split())
x, y, gcd = gcd_extended(a, b)

print(f"Maior divisor comum: {gcd}")
print(f"(x,y) = ({x},{y})")


# Encontrando uma solução de uma equação de diofantina linear com duas variáveis
def find_solution(a, b, c):
    if a == 0 and b == 0:
        if c == 0:
            return True, 0, 0  # Qualquer solução é válida
        else:
            return False, 0, 0

    x, y, gcd = gcd_extended(a, b)

    if a < 0:  # Multiplica x por -1 se a < 0
        x = -x
    if b < 0:
        y = -y

    if c % gcd != 0:  # checa se existe alguma solução
        return False, 0, 0

    t = c // gcd
    return True, x * t, y * t


a, b, c = map(int, input().split())
has_solution, x, y = find_solution(a, b, c)

if not has_solution:
    print("Não existe solução")
else:
    print(f"Solução: {x} {y}")
