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
        if self * other != 0:
            return self * other > 0

        return self % self < other % other


def counter_clockwise(a, b, c):
    return (b - a) * (c - a) > 0


# Dado um conjunto de pontos, ela retorna o fecho convexo desse conjunto no sentido anti-horário
def find_convex_hull(S):
    A = S[0]

    for i in range(len(S)):
        if S[i].y < A.y or (S[i].y == A.y and S[i].x < A.x):  # Acha uma nova origem
            A = S[i]

    for i in range(len(S)):
        S[i] = S[i] - A  # Translada todo os pontos, ou seja A é a origem

    S.sort()

    convex_hull = []

    for i in range(len(S)):
        while len(convex_hull) >= 2:
            p = len(convex_hull) - 1

            if counter_clockwise(convex_hull[p - 1], convex_hull[p], S[i]):
                break

            convex_hull.pop()

        convex_hull.append(S[i])

    for i in range(len(convex_hull)):
        convex_hull[i] = convex_hull[i] + A  # Translada os nossos pontos de volta

    return convex_hull


n = int(input())
S = []

for i in range(n):
    x, y = map(int, input().split())
    S.append(Point(x, y))

convex_hull = find_convex_hull(S)

print("Pontos do fecho convexo: ", end="")

for i in range(len(convex_hull)):
    print(f"({convex_hull[i].x},{convex_hull[i].y}) ", end="")

# Modificação para pontos colineares
# def counterclockwise(a, b, c):
#     return (b - a)*(c - a) >= 0 # Eles podem ser colineares

# def find_convex_hull(S):
#     A = S[0]
#
#     for i in range(len(S)):
#         if S[i].y < A.y or (S[i].y == '   A.y and S[i].x < A.x):
#             A = S[i]
#
#     for i in range(len(S)):
#         S[i] = S[i] - A
#
#     s.sort()
#
#     for i in range(len(S) - 1,0,-1): # Invertendo a última linha
#         if S[i]*S[i - 1] != 0 or i == 1:
#             S[i:] = S[i:][::-1] # Invertendo o sufixo achado
#             break
#
#     convex_hull = []
#
#     for i in range(len(S)):
#         while len(convex_hull) >= 2:
#             p = len(convex_hull) - 1
#
#             if counterclockwise(convex_hull[p - 1], convex_hull[p], s[i]):
#                 break
#
#             convex_hull.pop()
#
#         convex_hull.append(s[i])
#
#     for i in range(len(convex_hull)):
#         convex_hull[i] = convex_hull[i] + A
#
#     return convex_hull
