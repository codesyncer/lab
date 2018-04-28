from Trie import *


def main():
    my_trie = Trie()
    file = open('text.txt', 'r')
    word = ''
    line_c = 1
    for line in file:
        col_c = 1
        for ch in line:
            if ch.isalpha():
                word += ch
            elif len(word) > 0:
                my_trie.insert(word, (line_c, col_c))
                word = ''
            col_c += 1
        line_c += 1
    file.close()
    print(my_trie.search('the'))
    print(my_trie.match_prefix('se'))


if __name__ == '__main__':
    main()
