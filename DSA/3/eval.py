def isOperator(sym):
	return sym in ['+', '-', 'x', '/', '^']

def apply(op1, op2, op):
	if op == '+':
		return op1 + op2
	if op == '-':
		return op1 - op2
	if op == 'x':
		return op1 * op2
	if op == '/':
		if op2 == 0:
			return False
		return op1 / op2
	if op == '^':
		try:
			return op1 ** op2
		except:
			return False
	return False

def eval(ip):
	ip = ip.split()
	stack = []
	for sym in ip:
		if isOperator(sym):
			if not stack:
				return False
			op2 = stack.pop()
			if not stack:
				return False
			op1 = stack.pop()
			res = apply(op1, op2, sym)
			if res is False:
				return False
			stack.append(res)
		else:
			try:
				stack.append(float(sym))
			except:
				return False
	if len(stack) == 1:
		val = stack.pop()
		return int(val) if val.is_integer() else val
	return False

val = eval('8 3 5 7 + x /')
if 	val is False:
	print('Error')
else:
	print(val)