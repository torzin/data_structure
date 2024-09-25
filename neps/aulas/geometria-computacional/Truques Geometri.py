# Rotacionando Pontos
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Dado um ponto P e um ângulo teta (em radianos), retorna o ponto P rotacionado teta radianos em relação a origem no
# sentido anti-horário
def rotate(P, theta):
    x = P.x*math.cos(theta) - P.y*math.sin(theta)
    y = P.x*math.sin(theta) + P.y*math.cos(theta)

    return Point(x, y)


# Área dos triângulos
def areaTriangle(A, B, C):
    area = abs((B - A) * (C - A))
    return area/2


def areaTriangle(a, b, c):
    p = (a + b + c)/2
    area = p*(p - a)*(p - b)*(p - c)

    return math.sqrt(area)