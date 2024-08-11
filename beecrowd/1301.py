# Using SegTree
def _build(p, l, r):
    m = (l + r) // 2
    if l == r:
        st[p] = a[l]
        return st[p]
    st[p] = _build(p * 2, l, m) * _build(p * 2 + 1, m + 1, r)
    return st[p]


def _query(p, l, r, i, j):
    if r < i or l > j: return 1
    if i <= l and r <= j: return st[p]
    m = (l + r) // 2
    return _query(p * 2, l, m, i, j) * _query(p * 2 + 1, m + 1, r, i, j)


def _update(p, l, r, i, val):
    if i < l or i > r: return st[p]
    if i == l and l == r:
        st[p] = val
        return st[p]
    m = (l + r) // 2
    st[p] = _update(p * 2, l, m, i, val) * _update(p * 2 + 1, m + 1, r, i, val)
    return st[p]


while True:
    try:
        ans = ''

        n, k = input().split()
        n = int(n)
        k = int(k)

        a = list(map(int, input().split()))
        st = [0] * len(a) * 4

        _build(1, 0, n - 1)
        while k:
            k -= 1
            char, n1, n2 = input().split()
            n1, n2 = int(n1) - 1, int(n2)
            if char == "C":
                if n2:
                    n2 = abs(n2) // n2
                _update(1, 0, n - 1, n1, n2)
            elif char == 'P':
                n2 -= 1
                query_ans = _query(1,0, n - 1, n1, n2)
                if query_ans > 0:
                    ans += "+"
                elif query_ans < 0:
                    ans += '-'
                else:
                    ans += '0'
        print(ans)

    except EOFError:
        break
