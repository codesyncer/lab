class ListNode:
    def __init__(self, value = None, nxt = None):
        self.value = value
        self.next = nxt


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_head(self, x):
        self.head = ListNode(x, self.head)

    def delete(self, p):
        p.next = p.next.next

    def search(self, x):
        tmp = self.head
        while tmp is not None and tmp.value[0] != x:
            tmp = tmp.next
        return tmp

    def keys(self):
        l = []
        tmp = self.head
        while tmp is not None:
            l.append(tmp.value[0])
            tmp = tmp.next
        return l


class Hashtab:
    def __init__(self):
        self.arr = [None for i in range(30)]

    def hash(self, key):
        h = 0
        x = 33
        for ch in key:
            h *= x
            h += ord(ch)
        return h%30

    def insert(self, tup):
        hkey = self.hash(tup[0])
        if self.arr[hkey] is None:
            self.arr[hkey] = LinkedList()
        ll = self.arr[hkey]
        ll.insert_head(tup)
    
    def search(self, key):
        hkey = self.hash(key)
        return self.arr[hkey].search(key)

    def keys(self):
        ks = []
        for ll in self.arr:
            if ll is not None:
                ks += ll.keys()
        return ks


def main():
    dict = Hashtab()
    file = open('ispell.dict', 'r')
    for word in file:
        dict.insert((word[:-1], ))
    file.close()
    res = dict.search('cat')
    res = False if res is None else True
    print(res)

if __name__ == '__main__':
    main()