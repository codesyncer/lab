class TreeNode:
    def __init__(self, value=None, parent=None, left=None, right=None):
        self.parent = parent
        self.value = value
        self.left = left
        self.right = right
        self.h = 1

    @staticmethod
    def height(node):
        return 0 if node is None else node.h

    def re_calc_height(self):
        old_height = self.h
        hl = 0 if self.left is None else self.left.h
        hr = 0 if self.right is None else self.right.h
        self.h = max(hl, hr) + 1
        return old_height != self.h

    def is_leaf(self):
        return self.left is None and self.right is None


class AVLTree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, value):
        node = TreeNode(value)
        if self.root is None:
            self.root = node
            return
        tmp = self.root
        parent = None
        while tmp is not None:
            parent = tmp
            tmp = tmp.left if value <= tmp.value else tmp.right
        node.parent = parent
        if value <= parent.value:
            parent.left = node
        else:
            parent.right = node
        x = None
        y = node
        z = node.parent
        while z is not None and AVLTree.is_balanced(z):
            if not z.re_calc_height():
                return
            x = y
            y = z
            z = z.parent
        if z is None:
            return
        self.balance(z, y, x)

    def balance(self, z, y, x):
        if z.left == y and y.left == x:
            self.rotate_right(z)
            root = y
        elif z.left == y and y.right == x:
            self.rotate_left(y)
            self.rotate_right(z)
            root = x
        elif z.right == y and y.right == x:
            self.rotate_left(z)
            root = y
        else:
            self.rotate_right(y)
            self.rotate_left(z)
            root = x
        return root

    @staticmethod
    def is_balanced(node):
        return abs(TreeNode.height(node.left) - TreeNode.height(node.right)) <= 1

    def rotate_right(self, z):
        y = z.left
        z.left = y.right
        if y.right is not None:
            y.right.parent = z
        y.right = z
        y.parent = z.parent
        z.parent = y
        z.re_calc_height()
        y.re_calc_height()
        if y.parent is not None:
            if z == y.parent.left:
                y.parent.left = y
            else:
                y.parent.right = y
            y.parent.re_calc_height()
        else:
            self.root = y
        return y

    def rotate_left(self, z):
        y = z.right
        z.right = y.left
        if y.left is not None:
            y.left.parent = z
        y.left = z
        y.parent = z.parent
        z.parent = y
        z.re_calc_height()
        y.re_calc_height()
        if y.parent is not None:
            if z == y.parent.left:
                y.parent.left = y
            else:
                y.parent.right = y
            y.parent.re_calc_height()
        else:
            self.root = y
        return y

    @staticmethod
    def h(node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        hl = 0 if node.left is None else AVLTree.h(node.left)
        hr = 0 if node.right is None else AVLTree.h(node.right)
        return 1 + max(hl, hr)

    @staticmethod
    def print1(root, space):
        if root is None:
            return
        space += 5
        AVLTree.print1(root.right, space)
        i = 5
        while i < space:
            print(' ', end='')
            i += 1
        print(root.value)
        AVLTree.print1(root.left, space)

    def print(self):
        AVLTree.print1(self.root, 0)

    def search(self, value):
        tmp = self.root
        while tmp is not None and tmp.value != value:
            tmp = tmp.left if value < tmp.value else tmp.right
        return tmp

    @classmethod
    def successor(cls, node):
        if node is None:
            return
        if node.right is not None:
            return AVLTree(node.right).minimum()
        while node.parent is not None and node.parent.left != node:
            node = node.parent
        return node.parent

    @classmethod
    def predecessor(cls, node):
        if node is None:
            return
        if node.left is not None:
            return AVLTree(node.left).maximum()
        while node.parent is not None and node.parent.right != node:
            node = node.parent
        return node.parent

    def minimum(self):
        if self.root is None:
            return None
        tmp = self.root
        while tmp.left is not None:
            tmp = tmp.left
        return tmp

    def maximum(self):
        if self.root is None:
            return None
        tmp = self.root
        while tmp.right is not None:
            tmp = tmp.right
        return tmp

    def max(self, node):
        while node.right is not None:
            node = node.right
        return node

    def delete(self, node):
        if node is None:
            return

        if node.is_leaf():
            if node.parent is None:
                self.root = None
                return
            if node == node.parent.left:
                node.parent.left = None
            else:
                node.parent.right = None
            z = node.parent
            while True:
                while z is not None and AVLTree.is_balanced(z):
                    if not z.re_calc_height():
                        return
                    z = z.parent
                if z is None:
                    return
                z.re_calc_height()
                y = z.left if TreeNode.height(z.left) > TreeNode.height(z.right) else z.right
                x = y.left if TreeNode.height(y.left) > TreeNode.height(y.right) else y.right
                z = self.balance(z, y, x).parent
        else:
            if node.left is None or node.right is None:
                tmp = node.left if node.right is None else node.right
            else:
                tmp = AVLTree.predecessor(node)
            node.value = tmp.value
            self.delete(tmp)


tree = AVLTree()
test_data = open('avg.dat', 'r')
for line in test_data:
    tree.insert(int(line))
test_data.close()
test_data = open('avg.dat', 'r')
for line in test_data:
    if tree.search(int(line)) is None:
        print(':(')
        break
else:
    print('Done')
test_data.close()
count = 0
test_data = open('avg.dat', 'r')
for line in test_data:
    node = tree.search(int(line))
    print('\r' + line[:-1] + '\t' + str(count / 200) + '%', end='')
    if int(line) == 6979740377:
        x = 2
    if node is None:
        break
    else:
        tree.delete(node)
    count += 1
else:
    print('Done')
test_data.close()
