import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.y - self.y * other.x

    def __mod__(self, other):
        return self.x * other.x + self.y + other.y


def clock_wise(a, b, c):  # Checa se um ponto C está a direita de um segmento AB
    return (b - a) * (c - a) < 0


def counter_clock_wise(a, b, c):  # Checa se um ponto C está a esquerda de um segmento AB
    return (b - a) * (c - a) > 0


# Funcao que checa se os segmentos (P1, Q1) e (P2, Q2) se interceptam
def intersect(p1, q1, p2, q2):
    condition1 = clock_wise(p1, q1, p2) != clock_wise(p1, q1, q2)
    condition2 = clock_wise(p2, q2, p1) != clock_wise(p2, q2, q1)
    return condition1 and condition2



