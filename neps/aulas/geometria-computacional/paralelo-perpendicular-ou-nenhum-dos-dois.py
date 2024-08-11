class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __mul__(self, other):
        cross = self.x * other.y - self.y * other.x
        return cross

    def __mod__(self, other):
        dot = self.x * other.x + self.y * other.y
        return dot


def are_col(a, b):
    if a * b == 0:
        return True
    return False


def are_pen(a, b):
    if a % b == 0:
        return True
    return False


ax, ay, bx, by = map(int, input().split())
a = Point(ax, ay)
b = Point(bx, by)

if are_pen(a, b):
    print(-1)
elif are_col(a, b):
    print(1)
else:
    print(0)


