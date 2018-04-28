from MaxHeap import *
l = [10, 45, 21, 44, 22, 14, 20, 40, 100, 32, 56, 12, 54]
max_heap1 = MaxHeap()
for element in l:
    max_heap1.insert(element)
ssl = sorted(l, reverse=True)
sl1 = []
while max_heap1.maximum() is not None:
    sl1.append(max_heap1.extract_max())
print(ssl)
print(sl1)
max_heap2 = MaxHeap(l)
sl2 = []
while max_heap2.maximum() is not None:
    sl2.append(max_heap2.extract_max())
print(sl2)