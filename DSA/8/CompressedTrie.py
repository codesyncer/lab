class Node:
    def __init__(self, character=None):
        self.ch = character
        self.children = None
        self.indices = None

    def __eq__(self, other):
        return self.ch[0] == other[0]


class CompressedTrie:
    def __init__(self):
        self.root = Node()

    def insert(self, string, row_col=None):
        node = self.root
        i = 0
        while i < len(string):
            ch = string[i]
            if node.children is None:
                node.children = []
                node.children.append(Node(string[i:]))
                break
            try:
                node_str = node.children[node.children.index(ch)]

            except IndexError:
                pass
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
