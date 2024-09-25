class MaxHeap:
    def __init__(self):
        self.__v = [0]

    def insert(self, value):
        self.__v.append(value)
        self.__fix_insertion(len(self.__v) - 1)

    def get_maximum(self):
        return self.__v[1]

    def delete_maximum(self):
        self.__v[1], self.__v[-1] = self.__v[-1], self.__v[1]
        a = self.__v.pop()

        self.__fix_deletion(1)

        return a

    def __get_parent(self, node):
        return node//2

    def __get_left_child(self, node):
        return 2*node

    def __get_right_child(self, node):
        return 2*node + 1

    def __fix_insertion(self, node):
        if node == 1:
            return

        if self.__v[self.__get_parent(node)] > self.__v[node]:
            return

        self.__v[self.__get_parent(node)], self.__v[node] = self.__v[node],  self.__v[self.__get_parent(node)]
        self.__fix_insertion(self.__get_parent(node))

    def __fix_deletion(self, node):
        if self.__get_left_child(node) >= len(self.__v):
            return

        max_child = self.__get_left_child(node)

        if self.__get_right_child(node) < len(self.__v):
            if self.__v[self.__get_left_child(node)] <= self.__v[self.__get_right_child(node)]:
                max_child = self.__get_right_child(node)

        if self.__v[node] > self.__v[max_child]:
            return

        self.__v[node], self.__v[max_child] = self.__v[max_child], self.__v[node]
        self.__fix_deletion(max_child)

