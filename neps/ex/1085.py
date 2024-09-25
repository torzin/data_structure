def encontrar_dimensoes(A, B):
    # Tentamos todas as possíveis dimensões l e c
    for l in range(3, int((B + 4)**0.5) + 3):  # Começando de 3 já que precisamos de uma moldura
        if (B % (l-2)) == 0:
            c = (B // (l-2)) + 2  # As dimensões internas são (l-2) x (c-2)
            # Verificamos se a quantidade de azuis está correta
            if l * c - (l-2) * (c-2) == A:
                return min(l, c), max(l, c)
    return -1, -1


# Leitura da entrada
A = int(input())
B = int(input())

# Encontrar as dimensões e imprimir a resposta
largura, comprimento = encontrar_dimensoes(A, B)
print(largura, comprimento)
