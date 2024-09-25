def clockwise(a, b, c):
    return (b - a) * (c - a) < 0


def get_region(P, Q):
    n = len(P)

    if not clockwise(P[0], P[1], Q) or not clockwise(P[n - 1], P[0], Q):
        return 0

    l, r = 1, n - 1

    while l < r:
        m = (l + r) // 2

        if l == r - 1:
            m = r

        if clockwise(P[0], P[m], Q):
            l = m
        else:
            r = m - 1

    return l


def inside_polygon(P, Q):
    r = get_region(P, Q)
    print(r)

    if r == 0:
        return False

    return clockwise(P[r], P[r + 1], Q)