import sys
from math import sqrt, floor
from typing import List, Tuple


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __lt__(self, other):
        if self.x != other.x:
            return self.x < other.x
        return self.y < other.y


def distpointpoint(a: Point, b: Point) -> float:
    dx = b.x - a.x
    dy = b.y - a.y
    return sqrt(dx * dx + dy * dy)


def closestPoints(s: List[Point]) -> float:
    s.sort()
    p = 0
    activated = set()
    answer = distpointpoint(s[0], s[1])
    for i in range(len(s)):
        while s[i].x - s[p].x > answer:
            activated.remove((s[p].y, p))
            p += 1
        searchpoint = (s[i].y - floor(answer), 0)
        it = sorted([i for i in activated if i >= searchpoint])
        j = 0
        while j < len(it) and it[j][0] <= s[i].y + floor(answer):
            answer = min(answer, distpointpoint(s[it[j][1]], s[i]))
            j += 1
        activated.add((s[i].y, i))
    return answer


def main():
    n = int(input().strip())
    s = []
    for _ in range(n):
        x, y = map(int, input().strip().split())
        s.append(Point(x, y))
    print("{:.6f}".format(closestPoints(s)))


if __name__ == "__main__":
    sys.setrecursionlimit(10**9)
    main()

