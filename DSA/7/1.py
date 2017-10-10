class MaxHeap:
    def __init__(self, in_list=[]):
        self.arr = in_list
        self.build_heap()

    def parent_index(self, index):
        return (index - 1) // 2 if index != 0 else None

    def parent_value(self, index):
        return self.arr[self.parent_index(index)]

    def left_index(self, index):
        return 2 * index + 1 if 2 * index + 1 <= self.last_index() else None

    def left_value(self, index):
        return self.arr[self.left_index(index)]

    def right_index(self, index):
        return 2 * index + 2 if 2 * index + 2 <= self.last_index() else None

    def right_value(self, index):
        return self.arr[self.right_index(index)]

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

    def insert(self, key):
        index = len(self.arr)
        self.arr.append(key)
        parent_index = self.parent_index(index)
        while parent_index is not None and self.arr[parent_index] < self.arr[index]:
            self.swap(parent_index, index)
            index = parent_index
            parent_index = self.parent_index(index)

    def maximum(self):
        if len(self.arr) == 0:
            return None
        return self.arr[0]

    def extract_max(self):
        if len(self.arr) == 0:
            return None
        max_value = self.arr[0]
        self.arr[0] = self.arr[-1]
        self.arr.pop()
        self.heapify(0)
        return max_value

    def last_index(self):
        return len(self.arr) - 1

    def build_heap(self):
        if self.last_index() <= 0:
            return
        # n_of_elements = len(self.arr)
        for i in range(self.parent_index(self.last_index()), -1, -1):
            self.heapify(i)


l = [10, 45, 21, 44, 22, 14, 20, 40, 100, 32, 56, 12, 54]
mh1 = MaxHeap()
for element in l:
    mh1.insert(element)
ssl = sorted(l, reverse=True)
sl1 = []
while mh1.maximum() is not None:
    sl1.append(mh1.extract_max())
print(ssl)
print(sl1)
mh2 = MaxHeap(l)
sl2 = []
while mh2.maximum() is not None:
    sl2.append(mh2.extract_max())
print(sl2)
