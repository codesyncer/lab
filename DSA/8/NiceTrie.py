class ListNode:
    def __init__(self, value=None, nxt=None):
        self.value = value
        self.next = nxt


class MyList:
    def __init__(self):
        self.head = None

    @staticmethod
    def insert_after(x, p):
        p.next = ListNode(x, p.next)
        return p.next

    def insert_head(self, x):
        self.head = ListNode(x, self.head)
        return self.head

    def ordered_insert(self, x):
        if self.head is None or x < self.head.value:
            return self.insert_head(x)
        tmp = self.head
        while tmp.next is not None and tmp.next.value < x:
            tmp = tmp.next
        return self.insert_after(x, tmp)

    def search(self, x):
        tmp = self.head
        while tmp is not None and tmp.value != x:
            tmp = tmp.next
        return tmp

    def empty(self):
        return self.head is None


class Node:
    def __init__(self, character=None):
        self.ch = character
        self.children = None

    def __lt__(self, other):
        return ord(self.ch) < ord(other.ch)

    def __ne__(self, other):
        return self.ch != other


class NiceTrie:
    def __init__(self):
        self.root = Node()

    def insert(self, string):
        node = self.root
        for ch in string:
            if node.children is None:
                node.children = MyList()
            result = node.children.search(ch)
            if result is None:
                node = node.children.ordered_insert(Node(ch)).value
            else:
                node = result.value

    def search(self, string):
        node = self.root
        for ch in string:
            if node.children is None:
                return False
            list_node = node.children.search(ch)
            if list_node is None:
                return False
            node = list_node.value
        return node.children is None
