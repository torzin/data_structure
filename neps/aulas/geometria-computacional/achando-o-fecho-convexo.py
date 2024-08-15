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

    def __lt__(self, other):
        if self.x != other.x:
            return self.x < other.x

        return self.y < other.y


def clockwise(a, b, c):
    return (b - a) * (c - a) < 0


def counter_clockwise(a, b, c):
    return (b - a) * (c - a) > 0


def find_convex_hull(s):
    s.sort()

    upper_hull = []
    for i in range(len(s)):
        while len(upper_hull) >= 2:
            p = len(upper_hull) - 1

            if clockwise(upper_hull[p - 1], upper_hull[p], s[i]):
                break

            upper_hull.pop()

        upper_hull.append(s[i])

    lower_hull = []

    for j in range(len(s)):
        while len(lower_hull) >= 2:
            p = len(lower_hull) - 1

            if counter_clockwise(lower_hull[p - 1], lower_hull[p], s[j]):
                break

            lower_hull.pop()

        lower_hull.append(s[j])

    convex_hull = []

    for i in range(len(upper_hull)):
        convex_hull.append(upper_hull[i])

    for i in range(len(lower_hull) - 2, 0, -1):
        convex_hull.append(lower_hull[i])

    return convex_hull


n = int(input())
s = []

for _ in range(n):
    x, y = map(int, input().split())
    s.append(Point(x, y))

convex_hull = find_convex_hull(s)[::-1]

print(len(convex_hull))
for point in range(len(convex_hull)):
    print(convex_hull[point].x, convex_hull[point].y)

