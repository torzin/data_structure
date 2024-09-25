class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        cross = self.x * other.y - self.y * other.x
        return cross



p = []

for i in range(3):
    x, y = map(int, input().split())
    p.append(Point(x, y))

area = (p[2] - p[0]) * (p[1] - p[0])
print(int(abs(area) / 2))
