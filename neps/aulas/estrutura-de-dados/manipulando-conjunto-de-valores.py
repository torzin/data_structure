class MaxHeap:
    def __init__(self):
        self.v = [0]

    def insert(self, node):
        self.v.append(node)
        self.fix_insertion(len(self.v) - 1)

    def fix_insertion(self, node):
        if node == 1:
            return

        if self.v[node] < self.v[node // 2]:
            return

        self.v[node], self.v[node // 2] = self.v[node // 2], self.v[node]
        self.fix_insertion(node // 2)

    def print_max(self):
        return self.v[1]

    def print_sec_max(self):
        left = 2
        right = 3

        if len(self.v) >= right + 1:
            return max(self.v[left], self.v[right])
        else:
            return self.v[left]

    def delete_max(self):
        self.v[1], self.v[-1] = self.v[-1], self.v[1]
        self.v.pop()

        self.fix_del(1)

    def fix_del(self, node):
        if node * 2 >= len(self.v) :
            return

        max_child = 2*node

        if 2 * node + 1 < len(self.v):
            if self.v[node * 2] <= self.v[node * 2 + 1]:
                max_child = node * 2 + 1

        if self.v[node] > self.v[max_child]:
            return

        self.v[node], self.v[max_child] = self.v[max_child], self.v[node]
        self.fix_del(max_child)


q = int(input())

mh = MaxHeap()

for _ in range(q):
    type_q = input().split()

    if type_q[0] == '1':
        mh.delete_max()

    if type_q[0] == '2':
        mh.insert(int(type_q[1]))

    if type_q[0] == '3':
        print(mh.print_max())

    if type_q[0] == '4':
        print(mh.print_sec_max())



