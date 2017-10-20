class TreeNode:
    def __init__(self, value=None, parent=None, left=None, right=None):
        self.parent = parent
        self.value = value
        self.left = left
        self.right = right

    def is_leaf(self):
        return True if self.left is None and self.right is None else False


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    @staticmethod
    def check_node(node):
        if node is None:
            return
        left_value = node.value - 1 if node.left is None else node.left.value
        right_value = node.value - 1 if node.right is None else node.right.value
        return node.value > left_value and node.value > right_value

    def is_binary_heap(self):
        if self.root is None:
            return True
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if node is not None:
                if not BinaryTree.check_node(node):
                    return False
            else:
                while queue:
                    none = queue.pop(0)
                    if none is not None:
                        return False
                return True
            queue.append(node.left)
            queue.append(node.right)
