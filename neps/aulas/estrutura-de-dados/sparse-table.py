import math

class SparseTable:
    def __init__(self, arr):
        self.n = len(arr)
        self.log = [0] * (self.n + 1)
        self._build_log()
        self._build_sparse_table(arr)

    def _build_log(self):

        for i in range(2, self.n + 1):
            self.log[i] = self.log[i // 2] + 1

    def _build_sparse_table(self, arr):
        k = self.log[self.n] + 1
        self.sparse_table = [[0] * k for _ in range(self.n)]

        for i in range(self.n):
            self.sparse_table[i][0] = arr[i]

        j = 1
        while (1 << j) <= self.n:
            i = 0
            while (i + (1 << j) - 1) < self.n:
                self.sparse_table[i][j] = max(
                    self.sparse_table[i][j - 1],
                    self.sparse_table[i + (1 << (j - 1))][j - 1]
                )
                i += 1
            j += 1

    def query(self, left, right):
        # Faz a consulta para o intervalo [left, right]
        j = self.log[right - left + 1]
        return max(self.sparse_table[left][j], self.sparse_table[right - (1 << j) + 1][j])


n, q = map(int, input().split())
v = list(map(int, input().split()))

st = SparseTable(v)

for _ in range(q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    print(st.query(l, r))
