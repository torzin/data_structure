import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.y - self.y * other.x

    def __mod__(self, other):
        return self.x * other.x + self.y * other.y


def distance_point_point(a, b):
    dX = a.x - b.x
    dY = a.y - b.y

    distance = math.sqrt(dX*dX + dY*dY)
    return distance


# Dados três pontos a, b e p, retorna a distância entre p e a reta que passa por a e b
def distance_line_point(a, b, p):
    ab = b - a
    ap = p - a

    distance = abs(ap*ab)  # Pega o valor absoluto entre o produto vetorial entre ab e ap
    distance /= distance_point_point(a, b)

    return distance


# Lê todas as coordenadas dos pontos
x_a, y_a = map(int, input().split())
x_b, y_b = map(int, input().split())
x_p, y_p = map(int, input().split())

# Cria os três pontos
a = Point(x_a, y_a)
b = Point(x_b, y_b)
p = Point(x_p, y_p)

print(f"Distância entre a reta e p: {distance_line_point(a, b, p)}")

