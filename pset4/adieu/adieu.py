import inflect
p = inflect.engine()

def main():
	names = []
	while True:
		try:
			name = input("Name: ").strip()
			if name == "":
				show_output(names)
				break
			names.append(name)
		except EOFError:
			show_output(names)
			break

def show_output(names):
	print(f"Adieu, adieu, to {p.join(tuple(names))}")

if __name__ == "__main__":
	main()
