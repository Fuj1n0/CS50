from pyfiglet import Figlet
import sys

figlet = Figlet()

def main():
	if len(sys.argv) == 3:
		if sys.argv[1] not in ["-f", "--font"]:
			exit()
		if sys.argv[2] not in figlet.getFonts():
			exit()

		figlet.setFont(font=sys.argv[2])
	elif len(sys.argv) != 1:
		exit()
	print_output()

def print_output():
	print("Ouput:", figlet.renderText(input("Input: ")))

def exit():
	sys.exit("Invalid usage")

if __name__ == "__main__":
	main()
