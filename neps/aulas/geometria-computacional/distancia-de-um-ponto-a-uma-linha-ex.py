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


def dist_pp(a, b):
    dx = a.x - b.x
    dy = a.y - b.y

    return math.sqrt(dx**2 + dy**2)


def dist_line(a, b, p):
    ab = b - a
    ap = p - a

    dist = abs(ap*ab)
    dist /= dist_pp(a, b)

    return dist


ax, ay = map(int, input().split())
bx, by = map(int, input().split())
px, py = map(int, input().split())

a = Point(ax, ay)
b = Point(bx, by)
p = Point(px, py)

print(dist_line(a, b, p))
