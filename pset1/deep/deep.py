def main():
	user_input = convert_to_42(input("What is the Answer to the Great Question of Life, the Universe and Everything? "))
	valid = ["42", "fortytwo"]
	if user_input in valid:
		print("Yes")
	else:
		print("No")

def convert_to_42(i):
	return i.replace("-","").replace(" ","").lower()

main()
