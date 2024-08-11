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


def dist_pp(a, b):
    dx = a.x - b.x
    dy = a.y - b.y

    return math.sqrt(dx**2 + dy**2)


def dist_line(a, b, p):
    ap = p - a
    ab = b - a

    dist = (abs(ap*ab))
    dist /= dist_pp(a, b)

    return dist

def dist_seg(a, b, p):
    if (p - a) % (b - a) < 0:
        return dist_pp(p, a)

    if (p - b) % (a - b) < 0:
        return dist_pp(p, b)

    return dist_line(a, b, p)


ax, ay = map(int, input().split())
bx, by = map(int, input().split())
px, py = map(int, input().split())

a = Point(ax, ay)
b = Point(bx, by)
p = Point(px, py)

print(dist_seg(a, b, p))



