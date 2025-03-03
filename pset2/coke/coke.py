def main():
	amount = 50
	accumulated = 0
	accepted = ['5', '10', '25']
	while True:
		print("Amount Due:", amount - accumulated)
		coin = input("Insert Coin: ").strip()
		if coin in accepted:
			accumulated += int(coin)
		if accumulated >= 50:
			print("Change Owed: ", accumulated - amount)
			break

if __name__ == "__main__":
	main()
