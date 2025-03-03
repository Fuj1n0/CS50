def main():
	grocery = take_grocery()
	for k, v in sorted(grocery.items()):
		print(v, k)

def take_grocery():
	grocery = {}
	while True:
		try:
			item = input().upper()
			if item not in grocery:
				grocery[item] = 0
			grocery[item] += 1
		except (EOFError, KeyboardInterrupt):
			return grocery


if __name__ == "__main__":
	main()
