def gcd(x, y):
    # Função para calcular o maior divisor comum de x e y
    while y:
        x, y = y, x%y
    return x


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)


def calculate_area(polygon: list) -> tuple[float, int]:
    polygon.append(polygon[0])

    ans = 0
    m = 0

    for i in range(len(polygon) - 1):

        vector = [polygon[i+1].x - polygon[i].x, polygon[i+1].y - polygon[i].y]
        m += gcd(abs(vector[0]), abs(vector[1]))

        pos = polygon[i].x * polygon[i + 1].y
        neg = polygon[i].y * polygon[i + 1].x

        ans += pos - neg

    return ans / 2, m


n = int(input())
poly = []
for i in range(n):
    x, y = map(int, input().split())
    poly.append(Point(x, y))

area, m = calculate_area(poly)
ans = int((abs(area) - m/2 + 1))
print(ans)