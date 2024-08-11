class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)


# Dado um polígono simples no sentido horário, retorna sua área
def calculate_area(polygon: list):
    polygon.append(polygon[0]) # tornando nosso poligono cíclico

    ans = 0

    for i in range(len(polygon) - 1):
        sum_y = polygon[i + 1].y + polygon[i].y
        diff_x = polygon[i + 1].x - polygon[i].x

        ans += sum_y * diff_x

    return ans/2


n = int(input())

polygon = []

# Lê os pontos no sentido horário
for i in range(n):
    x, y = map(int, input().split())
    polygon.append(Point(x, y))

print(f"área do polígono: {calculate_area(polygon)}")

