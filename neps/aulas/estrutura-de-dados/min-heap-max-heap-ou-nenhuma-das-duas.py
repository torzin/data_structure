import sys

def verificar_heap(numbers, n):
    is_min = True
    is_max = True

    # Verificar se a árvore é min-heap ou max-heap percorrendo de cima para baixo
    for i in range(1, n // 2 + 1):
        left_child = 2 * i
        right_child = 2 * i + 1

        # Verificar o filho esquerdo
        if left_child <= n:
            if numbers[i] > numbers[left_child]:
                is_min = False
            if numbers[i] < numbers[left_child]:
                is_max = False

        # Verificar o filho direito
        if right_child <= n:
            if numbers[i] > numbers[right_child]:
                is_min = False
            if numbers[i] < numbers[right_child]:
                is_max = False

        # Se já sabemos que não é nenhum dos dois, podemos sair do loop
        if not is_min and not is_max:
            return 0

    # Retornar -1 se for min-heap, 1 se for max-heap, 0 se for normal
    if is_min:
        return -1
    elif is_max:
        return 1
    else:
        return 0

def main():
    input = sys.stdin.read  # Leitura rápida
    data = input().splitlines()  # Ler todas as linhas de uma vez
    n, q = map(int, data[0].split())

    results = []

    # Processar cada árvore
    for i in range(1, q + 1):
        numbers = [0] + list(map(int, data[i].split()))  # Ler a árvore, indexando a partir de 1
        results.append(verificar_heap(numbers, n))

    # Imprimir todos os resultados de uma vez
    sys.stdout.write("\n".join(map(str, results)) + "\n")

if __name__ == "__main__":
    main()
