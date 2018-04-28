def main():
    str1 = input('Str1 : ')
    str2 = input('Str2 : ')
    str3 = input('Str3 : ')
    print('string  : ' + replace(str1, str2, str3))


def replace(string, query, replacer):
    if len(query) > len(string):
        return string
    i = 0
    while i < len(string):
        if string[i] == query[0]:
            found = True
            for j in range(1, len(query)):
                if not string[i + j] == query[j]:
                    found = False
                    break
            if found:
                string = string[:i] + replacer + string[i + len(query):]
                i = i + len(replacer) - 1
        i = i + 1
    return string


if __name__ == '__main__':
    main()
