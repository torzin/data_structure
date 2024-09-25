class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.first = None
        self.last = None
        self.sz = 0

    def is_empty(self):
        if self.sz == 0:
            return True
        return False

    def insert_front(self, data):
        if self.is_empty():
            self.first = Node(data)
            self.last = self.first
        else:
            new_node = Node(data)
            new_node.next = self.first
            self.first = new_node

        self.sz += 1

    def insert_back(self, data):
        if self.is_empty():
            self.last = Node(data)
            self.first = self.last
        else:
            new_node = Node(data)
            self.last.next = new_node
            self.last = new_node

        self.sz += 1

    def remove_front(self):
        if not self.is_empty():
            self.first = self.first.next
            self.sz -= 1

            if self.is_empty():
                self.first = None
                self.last = None

    def front(self):
        return self.first.data

    def back(self):
        return self.first.data

    def __sz(self):
        return self.sz

    def clear(self):
        while not self.is_empty():
            self.remove_front()

    def find(self, data):
        cur = self.first

        while cur is not None:
            if cur.data == data:
                return True
            cur = cur.next

        return False

    # Supondo que a lista ligada já esteja ordenada em ordem crescente, a seguinte função insere um elemento sem
    # quebrar a condição de ordenação da lista :
    def sorted_insertion(self, data):
        if self.is_empty() or data < self.first.data:
            self.insert_front(data)
        else:
            cur = self.first
            while cur.next.data < data:
                cur = cur.next

            new_node = Node(data)
            new_node.next = cur.next
            cur.next = new_node

        self.sz += 1


# Creating a Linked List using queue
class Queue:
    def __init__(self, q):
        self.q = LinkedList()

    def empty(self):
        return self.q.is_empty()

    def size(self):
        return self.q.sz

    def front(self):
        return self.q.front()

    def push_back(self, data):
        self.q.insert_back(data)

    def pop_front(self):
        self.q.remove_front()


# Creating a linked list using stack
class Stack:
    def __init__(self):
        self.s = LinkedList()

    def empty(self):
        return self.s.is_empty()

    def size(self):
        return self.s.sz

    def back(self):
        return self.s.front()

    def push_back(self, data):
        self.s.insert_front(data)

    def pop_back(self):
        self.s.remove_front()