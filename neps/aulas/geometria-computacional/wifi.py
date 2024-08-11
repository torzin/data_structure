import bisect

class Event:
    def __init__(self, x, yl, yr, type):
        self.yl = yl
        self.yr = yr
        self.x = x
        self.type = type

    def __lt__(self, other):
        return self.x < other.x


n = int(input())
sweep = []
for i in range(n):
    xd, yd, xu, yu = map(int, input().split())

    sweep.append(Event(xd, yd, yu, 0))
    sweep.append(Event(xu, yd, yu, 2))

sweep.sort()

ans = 0
map = {}

for i in range(2 * n):
    type = sweep[i].type
    bottom = sweep[i].yl
    upper = sweep[i].yr

    if type == 0:
        map[upper] = 0
        map[bottom] = 1
    else:
        if map[upper] == 0:
            ans += 1

        keys = sorted(map.keys())
        idx = keys.index(upper)
        if idx > 0:
            prev_key = keys[idx - 1]
            map[prev_key] = 1

        del map[upper]
        del map[bottom]

print(ans)
