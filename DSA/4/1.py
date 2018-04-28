from HashTable import *


def main():
    my_dict = HashTable()
    file = open('ispell.dict', 'r')
    for word in file:
        my_dict.insert((word[:-1],))
    file.close()
    word = input('Enter word : ').split()[0]
    for i in range(len(word)):
        for ch in range(ord('a'), ord('z')):
            if chr(ch) == word[i]:
                continue
            new = word[:i] + chr(ch) + word[i + 1:]
            if my_dict.search(new) is not None:
                print(new)


if __name__ == '__main__':
    main()
