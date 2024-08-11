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


def clock_wise(a, b, c):  # Checa se um ponto C está a direita de um segmento AB
    return (b - a) * (c - a) < 0


def is_intersect(p1, q1, p2, q2):
    cond1 = clock_wise(p1, q1, p2) != clock_wise(p1, q1, q2)
    cond2 = clock_wise(p2, q2, p1) != clock_wise(p2, q2, q1)
    if cond2 and cond1:
        return 1
    else:
        return 0


x, y = map(int, input().split())
p1 = Point(x, y)
x1, y1 = map(int, input().split())
q1 = Point(x1, y1)
x2, y2 = map(int, input().split())
p2 = Point(x2, y2)
x3, y3 = map(int, input().split())
q2 = Point(x3, y3)

print(is_intersect(p1, q1, p2, q2))

