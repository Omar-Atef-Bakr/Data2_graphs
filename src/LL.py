class Node:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.next = None

    def __repr__(self):
        return f'{self.value} -> {self.next} '


class LL:
    def __init__(self, head: Node = None):
        self.head: Node = head
        self.tail: Node = head

    def insert(self, node: Node):
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def __repr__(self):
        return self.head.__repr__()