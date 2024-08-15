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


# Dado um conjunto de pontos, ela retorna o fecho convexo desse conjunto no sentido horário
def find_convex_hull(s):
    s.sort()

    upper_hul = []  # pilha que armazena o fecho superior

    for i in range(len(s)):
        while len(upper_hul) >= 2:
            p = len(upper_hul) - 1  # Índice do último ponto do fecho superior

            if clockwise(upper_hul[p-1], upper_hul[p], s[i]):  # Checa se S[i] está a direita da linha dada
                break

            upper_hul.pop()

        upper_hul.append(s[i])

    lower_hull = []

    for j in range(len(s)):
        while len(lower_hull) >= 2:
            p = len(lower_hull) - 1

            if counter_clockwise(lower_hull[p - 1], lower_hull[p], s[j]):
                break

            lower_hull.pop()

        lower_hull.append(s[j])

    convex_hull = []

    for i in range(len(upper_hul)):
        convex_hull.append(upper_hul[i])

    for i in range(len(lower_hull) - 2, 0, -1):
        convex_hull.append(lower_hull[i])

    return convex_hull


n = int(input())
s = []

for i in range(n):
    x, y = map(int, input().split())
    s.append(Point(x, y))

convex_hull = find_convex_hull(s)

print("Pontos do fecho convexo: ", end="")

for i in range(len(convex_hull)):
    print(f"({convex_hull[i].x},{convex_hull[i].y}) ", end="")



















