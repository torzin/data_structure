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


def clock_wise(a, b, c):
    return (b - a) * (c - a) < 0


def counter_clock_wise(a, b, c):
    return (b - a) * (c - a) > 0


def left_righ(a, b, c):
    if clock_wise(a, b, c):
        return -1
    elif counter_clock_wise(a, b, c):
        return 1


x1, y1 = map(int, input().split())
a = Point(x1, y1)

x2, y2 = map(int, input().split())
b = Point(x2, y2)

x3, y3 = map(int, input().split())
c = Point(x3, y3)


ans = left_righ(a, b, c)
print(ans)



