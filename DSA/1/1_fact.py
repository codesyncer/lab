def fact(n):
    res = 1
    while n > 1:
        res = res * n
        n = n - 1
    return res

def re_fact(n):
    if n <= 1:
        return 1
    return n * re_fact(n - 1)

n = int(input('Enter a number : '))
if n < 0:
    print('Got negative number')
else:
    print(str(n) + '! = ', fact(n))
    print(str(n) + '! by recursion = ', re_fact(n))
