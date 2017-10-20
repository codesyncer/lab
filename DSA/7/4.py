from MinHeap import *
l = [10, 45, 21, 44, 22, 14, 20, 40, 100, 32, 56, 12, 54]
min_heap1 = MinHeap()
for element in l:
    min_heap1.insert(element)
ssl = sorted(l)
sl1 = []
while min_heap1.minimum() is not None:
    sl1.append(min_heap1.extract_min())
print(ssl)
print(sl1)
min_heap2 = MinHeap(l)
sl2 = []
while min_heap2.minimum() is not None:
    sl2.append(min_heap2.extract_min())
print(sl2)