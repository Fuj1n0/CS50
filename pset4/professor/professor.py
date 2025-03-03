import random

def main():
	level = get_level()
	score = 0
	for _ in range(10):
		a, b = generate_integer(level), generate_integer(level)
		answer = str(a + b)
		for i in range(4):
			if i == 3:
				print(f"{a} + {b} = {answer}")
				break
			result = input(f"{a} + {b} = ")
			if result == answer:
				score += 1
				break
			else:
				print("EEE")

def get_level():
	while True:
		try:
			level = int(input("Level: "))
			if level > 0 and level < 4:
				return level
		except ValueError:
			pass

def generate_integer(level):
	if level == 1:
		return random.randint(0, 9)
	elif level == 2:
		return random.randint(10, 99)
	else:
		return random.randint(100, 999)

if __name__ == "__main__":
	main()
