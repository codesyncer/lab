from random import randint


class TreeNode:
    def __init__(self, value=None, parent=None, left=None, right=None):
        self.parent = parent
        self.value = value
        self.left = left
        self.right = right
        self.h = 1

    @staticmethod
    def pre_order(root):
        if root is None:
            return
        print(root.value, end=' ')
        TreeNode.pre_order(root.left)
        TreeNode.pre_order(root.right)

    @staticmethod
    def h(node):
        return 0 if node is None else node.h

    def re_calc_height(self):
        hl = 0 if self.left is None else self.left.h
        hr = 0 if self.right is None else self.right.h
        self.h = max(hl, hr) + 1


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
        if y is None:
            return
        y.re_calc_height()
        z = y.parent
        while z is not None and abs(TreeNode.h(z.left) - TreeNode.h(z.right)) <= 1:
            org_zh = z.h
            z.re_calc_height()
            if org_zh == z.h:
                return
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
            z.re_calc_height()
            if x is not None:
                x.re_calc_height()
            y.re_calc_height()
            sub_tree_root = y
        elif z.right == y and y.right == x:
            z.right = y.left
            if y.left is not None:
                y.left.parent = z
            y.parent = z.parent
            z.parent = y
            y.left = z
            if x is not None:
                x.re_calc_height()
            z.re_calc_height()
            y.re_calc_height()
            sub_tree_root = y
        elif z.left == y and y.right == x:
            y.right = x.left
            if x.left is not None:
                x.left.parent = y
            x.left = y
            y.parent = x
            x.parent = z
            z.left = x
            y.re_calc_height()
            x.re_calc_height()
            z.re_calc_height()
            sub_tree_root = self.rotate(y, x, z)
        else:
            y.left = x.right
            if x.right is not None:
                x.right.parent = y
            x.right = y
            y.parent = x
            x.parent = z
            z.right = x
            y.re_calc_height()
            x.re_calc_height()
            z.re_calc_height()
            sub_tree_root = self.rotate(y, x, z)
        return sub_tree_root

    # def h(self, node):
    #     if node is None:
    #         return 0
    #     if node.left is None and node.right is None:
    #         return 1
    #     hl = 0 if node.left is None else self.h(node.left)
    #     hr = 0 if node.right is None else self.h(node.right)
    #     return 1 + max(hl, hr)

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
        if node.left is None and node.right is None:
            if node == self.root:
                self.root = None
                return
            if node == node.parent.left:
                node.parent.left = None
            else:
                node.parent.right = None
            z = node.parent
            y = None
            while True:
                while z is not None and abs(TreeNode.h(z.left) - TreeNode.h(z.right)) <= 1:
                    org_zh = z.h
                    z.re_calc_height()
                    if org_zh == z.h:
                        return
                    y = z
                    z = z.parent
                if z is None:
                    return
                z.re_calc_height()
                y = z.left if y == z.right else z.right
                # y = z.left if TreeNode.h(z.left) > TreeNode.h(z.right) else z.right
                x = y.left if TreeNode.h(y.left) > TreeNode.h(y.right) else y.right
                sub_tree_root = self.rotate(x, y, z)
                if sub_tree_root.parent is None:
                    self.root = sub_tree_root
                else:
                    if sub_tree_root.value <= sub_tree_root.parent.value:
                        sub_tree_root.parent.left = sub_tree_root
                    else:
                        sub_tree_root.parent.right = sub_tree_root
                z = sub_tree_root.parent

        elif node.left is None or node.right is None:
            if node == self.root:
                self.root = node.right if node.left is None else node.left
                self.root.parent = None
            else:
                child = node.left if node.right is None else node.right
                node.value = child.value
                self.delete(child)
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

    def pre_order(self):
        TreeNode.pre_order(self.root)
        print()


avlt = AVLTree()
l = []
for i in range(10):
    x = randint(0, 1000)
    if x not in l:
        l.append(x)
        avlt.insert(x)
print(l)
print(avlt.minVal())
print(avlt.maxVal())
print(avlt.predecessor(avlt.search(l[0])).value)
print(avlt.successor(avlt.search(l[0])).value)

# for x in l:
#     if avlt.search(x) is None:
#         print(':(')
#     else:
#         avlt.delete(avlt.search(x))

# avlt = AVLTree()
# test_data = open('small.dat', 'r')
# for line in test_data:
#     avlt.insert(int(line))
# test_data.close()
# print(avlt.root.h)
# test_data = open('small.dat', 'r')
# for line in test_data:
#     if avlt.search(int(line)) is None:
#         print(':(')
#         break
# else:
#     print('Done')
# test_data.close()
# test_data = open('small.dat', 'r')
# for line in test_data:
#     node = avlt.search(int(line))
#     if node is None:
#         print(':(')
#         print(line)
#         break
#     else:
#         avlt.delete(node)
# else:
#     print('Done')
# test_data.close()
# # print(avlt.h(avlt.root))
# # print(avlt.root.h)
# #