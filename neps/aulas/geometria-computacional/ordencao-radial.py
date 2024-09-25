class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __mod__(self, other):
        dot = self.x * other.x + self.y * other.y
        return dot

    def __mul__(self, other):
        cross = self.x * other.y - self.y * other.x
        return cross

    def region(self):
        if self.y > 0 or (self.y == 0 and self.x > 0):
            return 0

        return 1

    def __lt__(self, other):
        if self.region() != other.region():
            return self.region() < other.region()

        if self * other != 0:
            return self * other > 0

        return self % self < other % other


n = int(input())
S = []

for _ in range(n):
    x, y = map(int, input().split())
    S.append(Point(x, y))

S.sort()

for point in S:
    print(point.x, point.y)

