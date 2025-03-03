months = [
    "january",
    "february",
    "march",
    "april",
    "may",
    "june",
    "july",
    "august",
    "september",
    "october",
    "november",
    "december"
]

while True:
	try:
		date = input("Date: ")
		if "/" in date:
			month, day, year = date.split("/")
			month, day, year = int(month), int(day), int(year)
		elif "," in date:
			month, day, year = date.split(" ")
			month, day, year = month.strip().lower(), int(day.replace(",","")), int(year)
			for i in range(len(months)):
				if month == months[i] or months[i].startswith(month):
					month = i + 1
					break
		if month > 12 or day > 31:
			raise ValueError("invalid date")
		outdate = f"{year}-{month:02d}-{day:02d}"
		print(outdate)
	except:
		pass
	else:
		break
