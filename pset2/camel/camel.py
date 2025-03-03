def main():
	camelCase = input("camelCase: ").strip()
	snake_case = ""
	for ch in camelCase:
		if ch.isupper():
			ch = "_" + ch.lower()
		snake_case += ch
	print(f"snake_case: {snake_case}")

if __name__ == "__main__":
	main()
