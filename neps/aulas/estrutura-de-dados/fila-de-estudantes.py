class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.sz = 0

    def empty(self):
        if self.sz == 0:
            return True
        return False

    def insert_front(self, data):
        new_node = Node(data)
        if self.empty():
            self.first = new_node
            self.last = self.first

        else:
            self.first.prev = new_node
            new_node.next = self.first
            self.first = new_node

        self.sz += 1

    def insert_back(self, data):
        new_node = Node(data)
        if self.empty():
            self.first = new_node
            self.last = self.first

        else:
            new_node.prev = self.last
            self.last.next = new_node
            self.last = new_node

        self.sz += 1

    def remove_front(self):
        if self.empty():
            return ['0', '0']

        data = self.first.data

        self.first = self.first.next
        self.sz -= 1

        if self.empty():
            self.first = None
            self.last = None

        return data

    def remove_back(self):
        if self.empty():
            return ['0', '0']

        data = self.last.data

        self.last = self.last.prev
        self.sz -= 1

        if self.empty():
            self.first = None
            self.last = None

        return data


n = int(input())

ll = LinkedList()

for i in range(n):
    query = input().split()

    if query[0] == '1':
        ll.insert_front([query[1], query[2]])

    elif query[0] == '2':
        ll.insert_back([query[1], query[2]])

    elif query[0] == '3':
        print(*ll.remove_front())

    elif query[0] == '4':
        print(*ll.remove_back())
