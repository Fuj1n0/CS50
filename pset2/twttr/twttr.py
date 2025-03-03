def main():
	post =input("Input: ")
	vowels = ['a', 'e', 'i', 'o', 'u']
	print("Output: ", end="")
	for ch in post:
		if ch.lower() not in vowels:
			print(ch, end="")
	print()

if __name__ == "__main__":
	main()
