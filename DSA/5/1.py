class TreeNode:
    def __init__(self, value=None, parent=None, left=None, right=None):
        self.parent = parent
        self.value = value
        self.left = left
        self.right = right

    def preorder(root):
        if root is None:
            return
        print(root.value, end=' ')
        TreeNode.preorder(root.left)
        TreeNode.preorder(root.right)


class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, value):
        node = TreeNode(value)
        if self.root is None:
            self.root = node
            return
        trav = self.root
        parent = None
        while trav is not None:
            parent = trav
            trav = trav.left if value < trav.value else trav.right
        node.parent = parent
        if value <= parent.value:
            parent.left = node
        else:
            parent.right = node

    def search(self, value):
        trav = self.root
        while trav is not None and trav.value != value:
            trav = trav.left if value < trav.value else trav.right
        return trav

    def successor(self, node):
        if node is None:
            return
        if node.right is not None:
            return BinarySearchTree(node.right).minimum()
        while node.parent is not None and node.parent.left != node:
            node = node.parent
        return node.parent

    def predecessor(self, node):
        if node is None:
            return
        if node.left is not None:
            return BinarySearchTree(node.left).maximum()
        while node.parent is not None and node.parent.right != node:
            node = node.parent
        return node.parent

    def delete(self, node):
        if node is None:
            return
        if node.left is None or node.right is None:
            if node == self.root:
                self.root = node.right if node.left is None else node.left
                if self.root is not None:
                    self.root.parent = None
            else:
                if node.parent.left == node:
                    node.parent.left = node.right if node.left is None else node.left
                else:
                    node.parent.right = node.right if node.left is None else node.left
                if node.left is not None:
                    node.left.parent = node.parent
                if node.right is not None:
                    node.right.parent = node.parent
        else:
            pred = self.predecessor(node)
            node.value = pred.value
            self.delete(pred)

    def minimum(self):
        if self.root is None:
            return None
        trav = self.root
        while trav.left is not None:
            trav = trav.left
        return trav

    def maximum(self):
        if self.root is None:
            return None
        trav = self.root
        while trav.right is not None:
            trav = trav.right
        return trav

    def present(self, value):
        return False if self.search(value) is None else True

    def minVal(self):
        node = self.minimum()
        return None if node is None else node.value

    def maxVal(self):
        node = self.maximum()
        return None if node is None else node.value

    def preorder(self, root=None):
        TreeNode.preorder(self.root)
        print()

    def traverse(self):
        thislevel = [self.root]
        while thislevel:
            nextlevel = list()
            for n in thislevel:
                print(n.value, end=' ')
                if n.left:
                    nextlevel.append(n.left)
                if n.right:
                    nextlevel.append(n.right)
            print()
            thislevel = nextlevel


bst = BinarySearchTree()
bst.insert(20)
bst.insert(10)
bst.insert(5)
bst.insert(1)
bst.insert(7)
bst.insert(15)
bst.insert(30)
bst.insert(25)
bst.insert(21)
bst.insert(35)
bst.insert(32)
bst.insert(40)
for i in range(45):
    node = bst.search(i)
    if node is not None:
        p = bst.predecessor(node)
        s = bst.successor(node)
        st = 'x' if p is None else str(p.value)
        st += ' <= '
        st += str(node.value)
        st += ' <= '
        st += 'x' if s is None else str(s.value)
        print(st)