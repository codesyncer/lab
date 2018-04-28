def quick(arr, low, high):
    if low < high:
        q = partition(arr, low, high)
        quick(arr, low, q - 1)
        quick(arr, q + 1, high)


def partition(arr, low, high):
    x = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[high], arr[i + 1] = arr[i + 1], arr[high]
    return i + 1


l = sorted([2, 4, 2, 2, 5, 3, 6, 7, 3, 1])
quick(l, 0, len(l) - 1)
print(l)
