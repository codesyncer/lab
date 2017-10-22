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
        hl = 0 if self.left is None else self.left.h
        hr = 0 if self.right is None else self.right.h
        self.h = max(hl, hr) + 1

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
            z_old_height = z.h
            z.re_calc_height()
            if z_old_height == z.h:
                return
            x = y
            y = z
            z = z.parent
        if z is None:
            return
        if z.left == y and y.left == x:
            self.rotate_right(y, z)
        elif z.left == y and y.right == x:
            self.rotate_left(x, y)
            self.rotate_right(x, z)
        elif z.right == y and y.right == x:
            self.rotate_left(y, z)
        else:
            self.rotate_right(x, y)
            self.rotate_left(x, z)

    @staticmethod
    def is_balanced(node):
        return True if abs(TreeNode.height(node.left) - TreeNode.height(node.right)) <= 1 else False

    # Lower, Upper
    def rotate_right(self, y, z):
        z.left = y.right
        if y.right is not None:
            y.right.parent = z
        y.right = z
        y.parent = z.parent
        z.parent = y
        if y.parent is not None:
            if y.value <= y.parent.value:
                y.parent.left = y
            else:
                y.parent.right = y
        else:
            self.root = y
        z.re_calc_height()
        y.re_calc_height()

    # Lower, Upper
    def rotate_left(self, x, y):
        y.right = x.left
        if x.left is not None:
            x.left.parent = y
        x.left = y
        x.parent = y.parent
        y.parent = x
        if x.parent is not None:
            if x.value <= x.parent.value:
                x.parent.left = x
            else:
                x.parent.right = x
        else:
            self.root = x
        y.re_calc_height()
        x.re_calc_height()

    def h(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        hl = 0 if node.left is None else self.h(node.left)
        hr = 0 if node.right is None else self.h(node.right)
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

    def delete(self, node):
        if node is None:
            return
        if node.is_leaf():
            if node == self.root:
                self.root = None
                return
            if node == node.parent.left:
                node.parent.left = None
            else:
                node.parent.right = None
            y = node
            z = node.parent
            while True:
                while z is not None and AVLTree.is_balanced(z):
                    z_old_height = z.h
                    z.re_calc_height()
                    if z_old_height == z.h:
                        return
                    y = z
                    z = z.parent
                if z is None:
                    return
                z.re_calc_height()
                y = z.left if TreeNode.height(z.left) > TreeNode.height(z.right) else z.right
                # y = z.left if y == z.right else z.right
                # if y is None:
                #     return
                x = y.left if TreeNode.height(y.left) > TreeNode.height(y.right) else y.right
                if z.left == y and y.left == x:
                    self.rotate_right(y, z)
                    z = y.parent
                elif z.left == y and y.right == x:
                    self.rotate_left(x, y)
                    self.rotate_right(x, z)
                    z = x.parent
                    y = x
                elif z.right == y and y.right == x:
                    self.rotate_left(y, z)
                    z = y.parent
                else:
                    self.rotate_right(x, y)
                    self.rotate_left(x, z)
                    z = x.parent
                    y = x
        else:
            if node.left is None or node.right is None:
                leaf = node.left if node.right is None else node.right
            else:
                leaf = self.predecessor(node)
            node.value = leaf.value
            self.delete(leaf)


tree = AVLTree()
test_data = open('as.dat', 'r')
for line in test_data:
    tree.insert(int(line))
test_data.close()

test_data = open('as.dat', 'r')
for line in test_data:
    if tree.search(int(line)) is None:
        print(':(')
        break
else:
    print('Done')
test_data.close()
test_data = open('as.dat', 'r')
for line in test_data:
    node = tree.search(int(line))
    if node is None:
        print(':(')
        print(line)
        # tree.print()
        break
    else:
        tree.delete(node)
else:
    print('Done')
test_data.close()
