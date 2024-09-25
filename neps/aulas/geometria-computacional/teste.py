class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Sobrecarregando o operador de subtração para pontos
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    # Método para calcular o produto vetorial de dois pontos
    def cross_product(self, other):
        return self.x * other.y - self.y * other.x

    # Sobrecarregando o operador menor que para pontos
    def __lt__(self, other):
        if self.x != other.x:
            return self.x < other.x
        return self.y < other.y

def find_convex_hull(points):
    # Ordena os pontos
    points.sort()

    # Calcula a metade superior do casco convexo
    upper_hull = []
    for point in points:
        # Se o produto vetorial for menor ou igual a zero, retire o ponto da pilha
        while len(upper_hull) >= 2 and (upper_hull[-1] - upper_hull[-2]).cross_product(point - upper_hull[-1]) <= 0:
            upper_hull.pop()
        upper_hull.append(point)

    # Calcula a metade inferior do casco convexo
    lower_hull = []
    for point in points:
        # Se o produto vetorial for maior ou igual a zero, retire o ponto da pilha
        while len(lower_hull) >= 2 and (lower_hull[-1] - lower_hull[-2]).cross_product(point - lower_hull[-1]) >= 0:
            lower_hull.pop()
        lower_hull.append(point)

    # Mescla a metade superior e inferior do casco
    convex_hull = upper_hull[:-1] + lower_hull[::-1][:-1]

    return convex_hull

# Lê a entrada
n = int(input())
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append(Point(x, y))

# Encontra o casco convexo
convex_hull = find_convex_hull(points)

# Imprime o resultado
print(len(convex_hull))
for point in convex_hull:
    print(point.x, point.y)
