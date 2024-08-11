# Dados b, e, e m, retorne (b^e) mod m
def fast_exponentiation(b, e, m):
    if e == 0:
        return 1 % m

    ans = fast_exponentiation(b, e//2, m)  # Acha a resposta do noso subproblema
    ans = (ans*ans) % m  # Eleva a resposta ao quadrado e tira módulo m

    if e % 2 == 0:
        return ans

    return (ans*b) % m

b, e, m = map(int,input().split())
print(f"Resposta: {fast_exponentiation(b, e, m)}")
