def main():
    ls = input('Enter elements : ').split()
    for i in range(len(ls)):
        ls[i] = int(ls[i])
    print('Bubble sorted list :', bubble_sort(ls[:]), end=' ')
    print()
    print('Selection sorted list :', select_sort(ls[:]), end=' ')
    print()


def bubble_sort(ls):
    n = len(ls)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if ls[j] > ls[j + 1]:
                ls[j + 1], ls[j] = ls[j], ls[j + 1]
    return ls


def select_sort(ls):
    n = len(ls)
    for i in range(n - 1):
        min_pos = i
        for j in range(i + 1, n):
            if ls[min_pos] > ls[j]:
                min_pos = j
        ls[min_pos], ls[i] = ls[i], ls[min_pos]
    return ls

if __name__ == '__main__':
    main()