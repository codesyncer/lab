def main():
    n = int(input('Enter number of terms : '))
    if n < 0:
        print('Got negative number')
    else:
        print('Series : ', end=' ')
        print_series(n)
        print('Series by recursion : ', end=' ')
        print_re_series(n, 1, 1)


def print_series(n):
    curr = 1
    nxt = 1
    while n > 0:
        print(curr, end=' ')
        curr, nxt = nxt, curr + nxt
        n = n - 1
    print()


def print_re_series(n, curr, nxt):
    if n <= 0:
        print()
        return
    print(curr, end=' ')
    print_re_series(n - 1, nxt, curr + nxt)


if __name__ == '__main__':
    main()
