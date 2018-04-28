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

    def refresh_height(self):
        old_height = self.h
        hl = 0 if self.left is None else self.left.h
        hr = 0 if self.right is None else self.right.h
        self.h = max(hl, hr) + 1
        return old_height != self.h

    def leaf(self):
        return self.left is None and self.right is None

    def balanced(self):
        return -1 <= TreeNode.height(self.left) - TreeNode.height(self.right) <= 1


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
        while tmp is not None and tmp.value != value:
            parent = tmp
            tmp = tmp.left if value < tmp.value else tmp.right
        if tmp is not None:
            return
        node.parent = parent
        if value < parent.value:
            parent.left = node
        else:
            parent.right = node
        x = None
        y = node
        z = node.parent
        while z is not None and z.balanced():
            z.refresh_height()
            x = y
            y = z
            z = z.parent
        if z is not None:
            z.refresh_height()
            self.balance(z, y, x)

    def balance(self, z, y, x):
        if z.value == 7041450 or x.value == 7041450 or y.value == 7041450:
            pass
        if z.left == y and y.left == x:
            return self.rotate_right(z)
        if z.left == y and y.right == x:
            self.rotate_left(y)
            return self.rotate_right(z)
        if z.right == y and y.right == x:
            return self.rotate_left(z)
        if z.right == y and y.left == x:
            self.rotate_right(y)
            return self.rotate_left(z)
        print('Why')

    def rotate_right(self, z):
        y = z.left
        z.left = y.right
        if y.right is not None:
            y.right.parent = z
        y.right = z
        y.parent = z.parent
        z.parent = y
        z.refresh_height()
        y.refresh_height()
        if y.parent is not None:
            if z == y.parent.left:
                y.parent.left = y
            else:
                y.parent.right = y
            y.parent.refresh_height()
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
        z.refresh_height()
        y.refresh_height()
        if y.parent is not None:
            if z == y.parent.left:
                y.parent.left = y
            else:
                y.parent.right = y
            y.parent.refresh_height()
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
        print((root.value, root.h))
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
        if node.leaf():
            if node.parent is None:
                self.root = None
            elif node == node.parent.left:
                node.parent.left = None
            else:
                node.parent.right = None
            z = node.parent
            while z is not None:
                if not z.balanced():
                    y = z.left if TreeNode.height(z.left) > TreeNode.height(z.right) else z.right
                    x = y.left if TreeNode.height(y.left) > TreeNode.height(y.right) else y.right
                    z = self.balance(z, y, x)
                    if z is not None and not z.balanced():
                        print(z.value)
                else:
                    z.refresh_height()
                z = z.parent if z is not None else None
        else:
            if node.left is None or node.right is None:
                tmp = node.left if node.right is None else node.right
                if not tmp.leaf():
                    print(node.value)
                    # pass
            else:
                tmp = AVLTree.successor(node)
            node.value = tmp.value
            self.delete(tmp)


def main():
    tree = AVLTree()
    test_data = open('avg.dat')
    for line in test_data:
        tree.insert(int(line))
    test_data.close()
    test_data = open('avg.dat')
    for line in test_data:
        if tree.search(int(line)) is None:
            print(':(')
            break
    else:
        print('Done')
    test_data.close()
    # tree.print()
    # node = tree.search(7041450)
    test_data = open('avg.dat')
    for line in test_data:
        if int(line) == 7041569:
            print('fr')
        node = tree.search(int(line))
        if node is None:
            print(line)
            # tree.print()
            break
        tree.delete(node)
    else:
        print('Done')
    test_data.close()


if __name__ == '__main__':
    main()
