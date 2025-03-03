def main():
	percentage = get_percentage()
	if percentage <= 1:
		print("E")
	elif percentage >= 99:
		print("F")
	else:
		print(f"{percentage}%")

def get_percentage():
	while True:
		try:
			x, y = input("Fraction: ").split("/")
			if float(x) != int(x) or float(y) != int(y):
				raise ValueError("values can be integers")
			x, y = int(x), int(y)
			if x > y:
				raise ValueError("x can't be greater than y")
			return round(x * 100 / y)
		except (ValueError, ZeroDivisionError ):
			pass

if __name__ == "__main__":
	main()
