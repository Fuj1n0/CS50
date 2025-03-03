import requests, sys

try:
	if len(sys.argv) != 2:
		sys.exit("Missing command-line argument")
	n = float(sys.argv[1])
except ValueError:
	sys.exit("Command-line argument is not a number")

try:
	response = requests.get("https://api.coincap.io/v2/assets/bitcoin")
	data = response.json()
	current_price = float(data["data"]["priceUsd"])
	amount = current_price * n
	print(f"${amount:,.4f}")

except requests.RequestException:
	sys.exit("check your internet connection.")

