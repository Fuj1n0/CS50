import sys
from PIL import Image, ImageOps

def main():
    if len(sys.argv) == 3:
        first, second = sys.argv[1].split("."), sys.argv[2].split(".")
        if not first[-1] == second[-1]:
            sys.exit("Input and output have different extensions")
        else:
            shirt(sys.argv[1],sys.argv[2])
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")


def shirt(before,after):
    try:
        shirt = Image.open("shirt.png")
        with Image.open(before) as input:
            input = ImageOps.fit(input, shirt.size)
            input.paste(shirt, mask = shirt)
            input.save(after)
    except FileNoFoundError:
        sys.exit()

if __name__ == "__main__":
    main()
