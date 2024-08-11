class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)


def cal_area(poly: list):
    poly.append(poly[0])

    ans = 0

    for i in range(len(poly) - 1):
        sum_y = poly[i + 1].y + poly[i].y
        diff_x = poly[i + 1].x - poly[i].x

        ans += sum_y*diff_x

    return abs(ans//2)


n = int(input())

polygon = []

for i in range(n):
    x, y = map(int, input().split())
    polygon.append(Point(x, y))

ans = cal_area(polygon)
print(ans)
