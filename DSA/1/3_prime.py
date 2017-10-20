def main():
    n = int(input('Enter number : '))
    if n <= 0:
        print('Enter positive number')
    else:
        print('isPrime returned ' + str(isPrime(n)))


def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    main()
