import random

def main():
	level = get_level()
	secret = random.randint(1, level)
	while True:
		try:
			guess = int(input("Guess: "))
			if guess > secret:
				print("Too large!")
			elif guess < secret:
				print("Too small!")
			else:
				print("Just right!")
				break
		except ValueError:
			pass

def get_level():
	while True:
		try:
			level = int(input("Level: "))
			if level > 0:
				return level
		except ValueError:
			pass

if __name__ == "__main__":
	main()
