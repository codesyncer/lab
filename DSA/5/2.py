class TreeNode:
	def __init__(self, value = None, parent = None, left = None, right = None):
		self.parent = parent
		self.value = value
		self.left = left
		self.right = right

	def preorder(root):
		if root is None:
			return
		print(root.value, end = ' ')
		TreeNode.preorder(root.left)
		TreeNode.preorder(root.right)

	def postorder(root):
		if root is None:
			return
		TreeNode.postorder(root.left)
		TreeNode.postorder(root.right)
		print(root.value, end = ' ')

class ParseTree:
	def __init__(self, inp):
		self.root = ParseTree.makeTree(inp)

	def printPrefix(self):
		TreeNode.preorder(self.root)
		print()

	def printPostfix(self):
		TreeNode.postorder(self.root)
		print()

	def apply(x, op, y):
		if op is None:
			return
		x = float(x)
		y = float(y)
		if op == '+':
			return x+y
		if op == '-':
			return x-y
		if op == 'x':
			return x*y
		if op == '/':
			return x/y

	def evaluateTree(self, node = None):
		if node == None:
			node = self.root
		if node.left == None:
			return node.value
		return ParseTree.apply(self.evaluateTree(node.left), node.value, self.evaluateTree(node.right))

	def makeTree(inp):
		stack = []
		for sym in inp:
			if sym == '(':
				continue
			elif sym == ')':
				operand2 = stack.pop()
				operator = stack.pop()
				operand1 = stack.pop()
				operator.left = operand1
				operator.right = operand2
				operand1.parent = operator
				operand2.parent = operator
				stack.append(operator)
			else:
				stack.append(TreeNode(sym))
		return stack.pop()

inp = '( ( 5 + 5 ) x ( ( 5 / 5 ) / 6 ) )'
pt = ParseTree(inp.split())
pt.printPrefix()
pt.printPostfix()
print(pt.evaluateTree())