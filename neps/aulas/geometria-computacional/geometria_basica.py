class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, a):  # Soma de vetores
        return Point(self.x + a.x, self.y + a.y)

    def __sub__(self, a):  # Subtração de vetores
        return Point(self.x - a.x, self.y - a.y)

    def __mul__(self, a):  # Produto vetorial
        cross = self.x * a.y - self.y * a.x
        return cross

    def __mod__(self, a):
        dot = self.x * a.x + self.y * a.y
        return dot


# Funcao que verifica se dois vetores sao perpendiculares
def are_perpendicular(a, b):
    return a % b == 0


def are_collinear(a, b):
    return a * b == 0


