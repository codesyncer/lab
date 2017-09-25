class Calc:
	def __init__(self):
		pass

	def isOperator(sym):
		return sym in ['+', '-', 'x', '/', '^', 'AVG', 'MAX', 'MIN']

	class Answer:
		def __init__(self, val, error = None):
			self.val = val
			self.error = error

	def eval(ip):
		ip = ip.split()
		il = len(ip)
		stack = []
		i = 0
		while i < il - 1:
			if isOperator(sym):
				op, n = sym, ip[i+1]
				i += 1 
				for j in range(i, n + i):
					pass
			elif isOperand(sym):
				try:
					stack.append(float(sym))
				except:
					return False
			i += 1