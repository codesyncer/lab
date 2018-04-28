class ListNode:
    def __init__(self, val=None, nxt=None):
        self.val = val
        self.next = nxt


class MyList:
    def __init__(self):
        self.head = None
        self.iterable_node = None

    @staticmethod
    def insert_after(x, p):
        p.next = ListNode(x, p.next)
        return p.next

    def insert_head(self, x):
        self.head = ListNode(x, self.head)
        return self.head

    def ordered_insert(self, x):
        if self.head is None or x < self.head.val:
            return self.insert_head(x)
        tmp = self.head
        while tmp.next is not None and tmp.next.val < x:
            tmp = tmp.next
        return self.insert_after(x, tmp)

    def search(self, x):
        tmp = self.head
        while tmp is not None and tmp.val != x:
            tmp = tmp.next
        return tmp

    def empty(self):
        return self.head is None

    def __iter__(self):
        self.iterable_node = self.head
        return self

    def __next__(self):
        if self.iterable_node is None:
            raise StopIteration
        val = self.iterable_node.val
        self.iterable_node = self.iterable_node.next
        return val


class Node:
    def __init__(self, character=None):
        self.ch = character
        self.children = None
        self.indices = None

    def __lt__(self, other):
        return ord(self.ch) < ord(other.ch)

    def __ne__(self, other):
        return self.ch != other


class NiceTrie:
    def __init__(self):
        self.root = Node()

    def insert(self, string, row_col=None):
        node = self.root
        for ch in string:
            result = None
            if node.children is None:
                node.children = MyList()
            else:
                result = node.children.search(ch)
            if result is None:
                result = node.children.ordered_insert(Node(ch))
            node = result.val
        if row_col is not None:
            if node.indices is None:
                node.indices = []
            node.indices.append((row_col[0], row_col[1] - (len(string) - 1)))

    def present(self, string):
        node = self.root
        for ch in string:
            if node.children is None:
                return False
            list_node = node.children.search(ch)
            if list_node is None:
                return False
            node = list_node.val
        return node.children is None

    def search(self, string):
        node = self.root
        for ch in string:
            if node.children is None:
                return []
            list_node = node.children.search(ch)
            if list_node is None:
                return []
            node = list_node.val
        return node.indices
