class ListNode:
    def __init__(self, value=None, nxt=None):
        self.value = value
        self.next = nxt


class LinkedList:
    def __init__(self):
        self.head = ListNode()
        self.length = 0

    def insert(self, x, p):
        p.next = ListNode(x, p.next)
        self.length += 1

    def delete(self, p):
        p.next = p.next.next
        self.length -= 1

    def print(self):
        tmp = self.head.next
        while tmp is not None:
            print(tmp.value, end=' ')
            tmp = tmp.next
        print()

    def insert_at_index(self, x, i):
        tmp = self.head
        while i > 0:
            tmp = tmp.next
            if tmp is None:
                return False
            i -= 1
        self.insert(x, tmp)

    def search(self, x):
        tmp = self.head.next
        while tmp is not None and tmp.value != x:
            tmp = tmp.next
        return tmp

    def len(self):
        return self.length

    def empty(self):
        return self.length == 0
