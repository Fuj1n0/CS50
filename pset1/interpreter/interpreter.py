def main():
	expression = input("Expression: ").split(" ")
	a , op, b = expression
	print(interpreter(float(a),op.strip(),float(b)))

def interpreter(a, op, b):
	if op == "+":
		return a + b
	elif op == "-":
		return a - b
	elif op == "*":
		return a * b
	elif op == "/":
		return a / b


main()
