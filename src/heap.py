class Heap:
    def __init__(self, elements: list[tuple]):
        self.elements = elements
        self.last = len(elements) - 1
        self.build_min_heap()

    def build_min_heap(self):
        last_parent = (self.last-1)//2
        while last_parent >= 0:
            self.heapify(last_parent)
            last_parent -= 1

    def heapify(self, i):
        minimum = i
        l = self.left(i)
        r = self.right(i)

        if l > self.last:
            return

        if self.elements[l][2] < self.elements[minimum][2]:
            minimum = l

        if r <= self.last and self.elements[r][2] < self.elements[minimum][2]:
            minimum = r

        if minimum == i:
            return

        self.elements[minimum], self.elements[i] = self.elements[i], self.elements[minimum]
        self.heapify(minimum)

    def pop(self):
        minimum = self.elements[0]
        self.elements[0], self.elements[self.last] = self.elements[self.last], self.elements[0]
        self.last -= 1
        self.heapify(0)
        return minimum

    def search(self, node):
        for i in range(len(self.elements)):
            if self.elements[i][0] == node[0]:
                return i


    @staticmethod
    def left(i):
        return 2 * i + 1

    @staticmethod
    def right(i):
        return 2 * i + 2

    def heap_sort(self):
        res = []
        for i in range(len(self.nums)):
            res.append(self.pop())
        self.elements = res.copy()






