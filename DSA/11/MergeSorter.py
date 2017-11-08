from random import randint

left = None
right = None


def sort(arr):
    global left, right
    left = [_ for _ in range(len(arr))]
    right = [_ for _ in range(len(arr))]
    merge_sort(arr, 0, len(arr) - 1)
    return arr


def merge_sort(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)
        merge(arr, low, mid, high)


def merge(arr, low, mid, high):
    for i in range(low, mid + 1):
        left[i - low] = arr[i]
    for i in range(mid + 1, high + 1):
        right[i - (mid + 1)] = arr[i]
    li = 0
    max_li = mid - low
    ri = 0
    max_ri = high - (mid + 1)
    i = low
    while li <= max_li and ri <= max_ri:
        if left[li] < right[ri]:
            arr[i] = left[li]
            li += 1
        else:
            arr[i] = right[ri]
            ri += 1
        i += 1
    while li <= max_li:
        arr[i] = left[li]
        i += 1
        li += 1
    while ri <= max_ri:
        arr[i] = right[ri]
        i += 1
        ri += 1


if __name__ == '__main__':
    my_list = [randint(0, 1000) for _ in range(10)]
    print(sort(my_list[:]))
    my_list.sort()
    print(my_list)
