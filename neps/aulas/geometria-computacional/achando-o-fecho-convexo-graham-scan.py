class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        dot = self.x * other.y - self.y * other.x
        return dot

    def __mod__(self, other):
        cross = self.x * other.x - self.y * other.y
        return cross

    def __lt__(self, other):
        if self * other != 0:
            return self * other > 0

        return self % self < other % other


def counter_clockwise(a, b, c):
    return (b - a) * (c - a) > 0


def find_convex_hull(s):
    a = s[0]

    for i in range(len(s)):
        if s[i].y < a.y or (s[i].y == a.y and s[i].x < a.x):
            a = s[i]

    for i in range(len(s)):
        s[i] -= a

    s.sort()
    convex_hull = []

    for i in range(len(s)):
        while len(convex_hull) >= 2:
            p = len(convex_hull) - 1

            if counter_clockwise(convex_hull[p - 1], convex_hull[p], s[i]):
                break

            convex_hull.pop()

        convex_hull.append(s[i])

    for i in range(len(convex_hull)):
        convex_hull[i] += a

    return convex_hull


n = int(input())

s = []
for _ in range(n):
    x, y = map(int, input().split())
    s.append(Point(x, y))

convex_hull = find_convex_hull(s)
print(len(convex_hull))
for i in range(1, len(convex_hull)):
    print(convex_hull[i].x, convex_hull[i].y)
print(convex_hull[0].x, convex_hull[0].y)











