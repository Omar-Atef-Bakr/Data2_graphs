from heap import Heap

class Pqeue:
    def __init__(self, arr: list):
        self.heap = Heap(arr)

    def pop(self):
        return self.heap.pop()

    def empty(self):
        return self.heap.last == 0

    def update(self, edge):




# edges = [
#     ('a', 'b', 4),
#     ('a', 'h', 8),
#     ('h', 'b', 11),
#     ('c', 'b', 8),
#     ('h', 'i', 7),
#     ('c', 'i', 2),
#     ('h', 'g', 1),
#     ('i', 'g', 6),
#     ('f', 'g', 2),
#     ('c', 'f', 4),
#     ('c', 'd', 7),
#     ('d', 'f', 14),
#     ('e', 'f', 10),
#     ('d', 'e', 9)
# ]
#
# h = Heap(edges)
#
# print(h.elements)
