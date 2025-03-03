def main():
	user_input = input("Greeting: ").lower()
	score = 0
	if "how" in user_input:
		score += 20
	if "what" in user_input:
		score += 100
	print(f"${score}")

main()
