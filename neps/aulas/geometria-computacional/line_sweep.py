import bisect

class Event:
    def __init__(self, x, yl, yr, type):
        self.yl = yl
        self.yr = yr
        self.x = x
        self.type = type

    def __lt__(self, other):
        if self.x != other.x:
            return self.x < other.x

        return self.type < other.type


n, m = map(int, input().split())
sweep = []

for i in range(n):
    xd, yd, xu, yu = map(int, input().split())

    sweep.append(Event(xd, yd, yu, 0))
    sweep.append(Event(xu, yd, yu, 2))

for i in range(m):
    x, y = map(int, input().split())

    sweep.append(Event(x, y, y, 1))

sweep.sort()

ans = 0


intervals = []
for i in range(len(sweep)):
    type = sweep[i].type
    L = sweep[i].yl
    R = sweep[i].yr

    if type == 0:
        intervals.append((L, R))
    if type == 1:
        target = (L+1, 0)
        index = bisect.bisect_right(intervals, target)

        if index > 0:
            it = intervals[index - 1]

            if it[0] <= L <= it[1]:
                ans += 1
    if type == 2:
        intervals.pop(intervals.index((L, R)))


print(ans)


