import random
class TreeNode:
    def __init__(self, value=None, parent=None, left=None, right=None, height=None):
        self.parent = parent
        self.value = value
        self.left = left
        self.right = right
        self.h = height

    def preorder(root):
        if root is None:
            return
        print(root.value, end=' ')
        TreeNode.preorder(root.left)
        TreeNode.preorder(root.right)

    @staticmethod
    def h(node):
        return 0 if node is None else node.h

class AVLTree:
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
        x = node
        y = x.parent
        # y.h = max(y.h, x.h+1)
        if y is None:
            return
        z = y.parent
        # z.h = max(z.h, y.h+1)
        # ToDo continue O(1) height
        while z is not None and abs(self.h(z.left) - self.h(z.right)) <= 1:
            x = x.parent
            y = y.parent
            z = z.parent
        if z is None:
            return
        sub_tree_root = self.rotate(x, y, z)
        if sub_tree_root.parent is None:
            self.root = sub_tree_root
        else:
            if sub_tree_root.value <= sub_tree_root.parent.value:
                sub_tree_root.parent.left = sub_tree_root
            else:
                sub_tree_root.parent.right = sub_tree_root

    def rotate(self, x, y, z):
        if z.left == y and y.left == x:
            z.left = y.right
            if y.right is not None:
                y.right.parent = z
            y.parent = z.parent
            z.parent = y
            y.right = z
            sub_tree_root = y
        elif z.right == y and y.right == x:
            z.right = y.left
            if y.left is not None:
                y.left.parent = z
            y.parent = z.parent
            z.parent = y
            y.left = z
            sub_tree_root = y
        elif z.left == y and y.right == x:
            y.right = x.left
            if x.left is not None:
                x.left.parent = y
            x.left = y
            y.parent = x
            x.parent = z
            z.left = x
            sub_tree_root = self.rotate(y, x, z)
        else:
            y.left = x.right
            if x.right is not None:
                x.right.parent = y
            x.right = y
            y.parent = x
            x.parent = z
            z.right = x
            sub_tree_root = self.rotate(y, x, z)
        return sub_tree_root

    def h(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        hl = 0 if node.left is None else self.h(node.left)
        hr = 0 if node.right is None else self.h(node.right)
        return 1 + max(hl, hr)

    def search(self, value):
        trav = self.root
        while trav is not None and trav.value != value:
            trav = trav.left if value < trav.value else trav.right
        return trav

    def successor(self, node):
        if node is None:
            return
        if node.right is not None:
            return AVLTree(node.right).minimum()
        while node.parent is not None and node.parent.left != node:
            node = node.parent
        return node.parent

    def predecessor(self, node):
        if node is None:
            return
        if node.left is not None:
            return AVLTree(node.left).maximum()
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


bst = AVLTree()
l = []
for i in range(1000):
    x = random.randint(0, 1000000)
    if x not in l:
        l.append(x)
        bst.insert(l[-1])
for i in l:
    if bst.search(i) is None:
        print(':(')
        break
else:
    print('Done')