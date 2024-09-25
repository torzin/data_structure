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
        cross = self.x * other.y - self.y * other.x
        return cross

    def __mod__(self, other):
        dot = self.x * other.x + self.y * other.y
        return dot

    def region_value(self):
        if self.y > 0 or (self.y == 0 and self.x > 0):
            return 0

        return 1

    def __lt__(self, other):
        if self.region_value() != other.region_value():
            return self.region_value() < other.region_value()

        if self * other != 0:
            return self * other > 0

        return self % self < other % other


n = int(input())
S = []

for i in range(n):
    x, y = map(int, input().split())
    S.append(Point(x, y))

S.sort()
print("Ordenação do radial sweep: ",end="")

for point in S:
    print(f"({point.x},{point.y}) ",end="")