class MinHeap:
    def __init__(self, in_list=[]):
        self.arr = None
        self.build_heap(in_list)

    @classmethod
    def parent_index(cls, index):
        return (index - 1) // 2 if index != 0 else None

    def left_index(self, index):
        return 2 * index + 1 if 2 * index + 1 <= self.last_index() else None

    def right_index(self, index):
        return 2 * index + 2 if 2 * index + 2 <= self.last_index() else None

    def swap(self, index1, index2):
        self.arr[index1], self.arr[index2] = self.arr[index2], self.arr[index1]

    def heapify(self, index):
        li = self.left_index(index)
        ri = self.right_index(index)
        if li is None and ri is None:
            return
        if li is None or ri is None:
            mini = li if ri is None else ri
        else:
            mini = li if self.arr[li] < self.arr[ri] else ri
        if self.arr[mini] < self.arr[index]:
            self.swap(mini, index)
            self.heapify(mini)

    def insert(self, key):
        index = len(self.arr)
        self.arr.append(key)
        parent_index = self.parent_index(index)
        while parent_index is not None and self.arr[parent_index] > self.arr[index]:
            self.swap(parent_index, index)
            index = parent_index
            parent_index = self.parent_index(index)

    def minimum(self):
        if len(self.arr) == 0:
            return None
        return self.arr[0]

    def extract_min(self):
        if len(self.arr) == 0:
            return None
        max_value = self.arr[0]
        self.arr[0] = self.arr[-1]
        self.arr.pop()
        self.heapify(0)
        return max_value

    def last_index(self):
        return len(self.arr) - 1

    def build_heap(self, in_list):
        self.arr = in_list
        if self.last_index() <= 0:
            return
        for i in range(self.parent_index(self.last_index()), -1, -1):
            self.heapify(i)

    def empty(self):
        return self.arr is None or len(self.arr) == 0

    def update_priority(self):
        pass