import sys, os, csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif not os.path.isfile(sys.argv[1]):
    sys.exit(f"Could not read {sys.argv[1]}")
elif not sys.argv[1].endswith('.csv'):
    sys.exit("Not a CSV file")

with open(sys.argv[1], 'r') as before:
    before = csv.DictReader(before)
    with open(sys.argv[2], 'w') as after:
        writer = csv.DictWriter(after, fieldnames=['first', 'last', 'house'])
        writer.writeheader()
        for row in before:
            last, first = row['name'].split(',')
            house = row['house']
            writer.writerow(
                {'first': first.strip(), 'last': last, 'house': house}
            )
