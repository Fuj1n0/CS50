def main():
	plate = input("Plate: ")
	if is_valid(plate):
		print("Valid")
	else:
		print("Invalid")


def is_valid(plate):
	length = len(plate)
	if length > 6 or length < 2:
		return False
	if not (plate[0].isalpha() and plate[1].isalpha()):
		return False
	num_found = False
	for ch in plate[2:]:
		if ch.isdigit():
			if not num_found:
				if ch == '0':
					return False
				num_found = True
		if not ch.isalnum():
			return False
		if ch.isalpha() and num_found:
			return False
	return True

if __name__ == "__main__":
	main()
