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

    def __lt__(self, other):
        if self.x != other.x:
            return self.x < other.x

        return self.y < other.y


def clockwise(a, b, c):
    return (b - a) * (c - a) <= 0


def counter_clockwise(a, b, c):
    return (b - a) * (c - a) >= 0


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

    for i in range(len(s)):
        while len(lower_hull) >= 2:
            p = len(lower_hull) - 1

            if counter_clockwise(lower_hull[p - 1], lower_hull[p], s[i]):
                break

            lower_hull.pop()

        lower_hull.append(s[i])

    new_s = s

    for i in range(len(upper_hull)):
        new_s.pop(new_s.index(upper_hull[i]))

    for i in range(len(lower_hull) - 2, 0, -1):
        new_s.pop(new_s.index(lower_hull[i]))

    return new_s, len(upper_hull) + len(lower_hull) - 2


while True:
    n = int(input())

    if n == 0:
        break

    s = []
    for _ in range(n):
        x, y = map(int, input().split())
        s.append(Point(x, y))

    count = 0
    while s:
        s, len_conv = find_convex_hull(s)
        if len_conv >= 3:
            count += 1

    if count % 2 == 0:
        print('Do not take this onion to the lab!')
    else:
        print('Take this onion to the lab!')
