from BinaryTree import *

bt = BinaryTree(TreeNode(14))
bt.root.left = TreeNode(13)
bt.root.right = TreeNode(8)
bt.root.left.left = TreeNode(12)
bt.root.left.right = TreeNode(5)
bt.root.right.left = TreeNode(6)
bt.root.right.right = TreeNode(4)

print(bt.is_binary_heap())
