import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mod__(self, other):
        return self.x * other.x + self.y * other.y

    def __mul__(self, other):
        return self.x * other.y - self.y * other.x


def distance_point_point(a, b):
    dx = a.x - b.x
    dy = a.y - b.y

    distance = math.sqrt(dx**2 + dy**2)
    return distance


def distance_line_point(a, b, p):
    ab = b - a
    ap = p - a

    distance = abs(ap*ab)  # Pega o valor absoluto entre o produto vetorial entre ab e ap
    distance /= distance_point_point(a, b)

    return distance


# Dados três pontos a, b e p, retorna a distância entre p e o segmento ab
def distance_segment_point(a, b, p):
    if (p-a) % (b - a) < 0:
        return distance_point_point(p, a)

    if (p - b) % (a - b) < 0:
        return distance_point_point(p, b)

    return distance_line_point(a, b, p)


x_a, y_a = map(int, input().split())
x_b, y_b = map(int, input().split())
x_p, y_p = map(int, input().split())

a = Point(x_a, y_a)
b = Point(x_b, y_b)
p = Point(x_p, y_p)

print(f"Distância entre o segmento e p: {distance_segment_point(a, b, p)}")



