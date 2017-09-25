class ListNode:
    def __init__(self, value = None, nxt = None):
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
        while tmp != None:
            print(tmp.value, end = ' ')
            tmp = tmp.next
        print()

    def insertAtIndex(self, x, i):
        tmp = self.head
        while i > 0:
            tmp = tmp.next
            if tmp == None:
                return False
            i -= 1
        self.insert(x, tmp)
        
    def search(self, x):
        tmp = self.head.next
        while tmp != None and tmp.value != x:
            tmp = tmp.next
        return tmp

    def len(self):
        return self.length

    def isEmpty(self):
        return self.length == 0

def main():
    L = LinkedList()
    L.insert(10, L.head)
    print('List is: ', end = '')
    L.print()
    L.insert(12, L.head.next)
    print('List is: ', end = '')
    L.print()
    L.insert(2, L.head)
    print('List is: ', end = '')
    L.print()
    print('Size of List:', L.len())
    L.delete(L.head)
    print('List is: ', end = '')
    L.print()
    L.delete(L.head.next)
    print('List is: ', end = '')
    L.print()
    print('List is empty?', L.isEmpty())
    print('Size of L is:', L.len())
    L.delete(L.head)
    print('List is empty?', L.isEmpty())
    print('Size of L is:', L.len())
    L.insertAtIndex(2, 0)
    L.insertAtIndex(1, 0)
    L.insertAtIndex(4, 2)
    L.insertAtIndex(3, 2)
    print('List is: ', end = '')
    L.print()

if __name__ == '__main__':
    main()