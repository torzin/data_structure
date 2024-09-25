N = 100005


def make_vector(a, b):
    return b[0] - a[0], b[1] - a[1]


def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]


def cross2(O, A, B):
    return (A[0] - O[0]) * (B[1] - O[1]) - (A[1] - O[1]) * (B[0] - O[0])


def S(A, B, C):
    return abs(cross2(A, B, C))


n, m = map(int, input().split())
v = [tuple(map(int, input().split())) for _ in range(n)]
v.sort()

hull = []
for i in range(n):
    while len(hull) >= 2 and cross(make_vector(hull[-2], hull[-1]), make_vector(hull[-1], v[i])) >= 0:
        hull.pop()
    hull.append(v[i])

lhull = []
for i in range(n - 1, -1, -1):
    while len(lhull) >= 2 and cross(make_vector(lhull[-2], lhull[-1]), make_vector(lhull[-1], v[i])) >= 0:
        lhull.pop()
    lhull.append(v[i])

lhull.reverse()
while lhull:
    if lhull[-1] != hull[-1]:
        hull.append(lhull[-1])
    lhull.pop()

if hull[-1] == hull[0]:
    hull.pop()

P = hull[0]
ans = 0
v, hull = hull, v
n = len(v)

for _ in range(m):
    x, y = map(int, input().split())
    Q = (x, y)
    ini, fim = 1, n - 1
    id = -1
    while fim >= ini:
        mid = (ini + fim) // 2
        if cross2(P, Q, v[mid]) >= 0:
            id = mid
            ini = mid + 1
        else:
            fim = mid - 1
    can = True
    if id >= n or id == -1:
        can = False
    if can:
        if id + 1 < n:
            Stot = S(P, v[id], v[id + 1])
            S1 = S(P, v[id], Q)
            S2 = S(P, v[id + 1], Q)
            S3 = S(Q, v[id], v[id + 1])
            if Stot != S1 + S2 + S3:
                can = False
        else:
            U = cross2(P, Q, v[n - 1])
            xmin = min(P[0], v[n - 1][0])
            xmax = max(P[0], v[n - 1][0])
            if U != 0 or not (xmin <= Q[0] <= xmax):
                can = False
    if can:
        ans += 1

print(ans)
