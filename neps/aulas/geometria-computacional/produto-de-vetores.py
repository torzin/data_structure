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


ax, ay, bx, by = map(int, input().split())
a = Point(ax, ay)
b = Point(bx, by)

print(a % b, end=" ")
print(a * b)
