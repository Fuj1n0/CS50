def main():
	extension = input("File name: ").strip().lower().split(".")[-1]
	print(get_extension(extension))

def get_extension(e):
	if e in ["jpg", "jpeg"]:
		return "image/jpeg"
	elif e == "gif":
		return "image/gif"
	elif e == "png":
		return "image/png"
	elif e == "pdf":
		return "application/pdf"
	elif e == "txt":
		return "text/plain"
	elif e == "zip":
		return "application/zip"
	else:
		return "application/octet-stream"


main()
