class HeapSorter:
    def __init__(self, in_list=[]):
        self.arr = self.last_index = None
        self.build_heap(in_list)

    @classmethod
    def parent_index(cls, index):
        return (index - 1) // 2 if index != 0 else None

    def left_index(self, index):
        return 2 * index + 1 if 2 * index + 1 <= self.last_index else None

    def right_index(self, index):
        return 2 * index + 2 if 2 * index + 2 <= self.last_index else None

    def swap(self, index1, index2):
        self.arr[index1], self.arr[index2] = self.arr[index2], self.arr[index1]

    def heapify(self, index):
        li = self.left_index(index)
        ri = self.right_index(index)
        if li is None and ri is None:
            return
        if li is None or ri is None:
            maxi = li if ri is None else ri
        else:
            maxi = li if self.arr[li] > self.arr[ri] else ri
        if self.arr[maxi] > self.arr[index]:
            self.swap(maxi, index)
            self.heapify(maxi)

    def extract_max(self):
        if len(self.arr) == 0:
            return None
        max_value = self.arr[0]
        self.arr[0] = self.arr[self.last_index]
        self.last_index -= 1
        self.heapify(0)
        return max_value

    def build_heap(self, in_list):
        self.arr = in_list
        self.last_index = len(self.arr) - 1
        if self.last_index <= 0:
            return
        for i in range(self.parent_index(self.last_index), -1, -1):
            self.heapify(i)

    def size(self):
        return self.last_index + 1

    @staticmethod
    def sort(in_list):
        max_heap = HeapSorter(in_list)
        size = max_heap.size()
        for i in range(size - 1, 0, -1):
            in_list[i] = max_heap.extract_max()
