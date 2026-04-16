import csv, sys

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

input_file = sys.argv[1]
output_file = sys.argv[2]

if input_file.split(".")[1] != "csv":
    sys.exit("Not a CSV file")
try:
    with open(input_file) as infile, open(output_file, "w") as outfile:
        reader = csv.DictReader(infile)
        fieldnames = ['first', 'last', 'house']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            last, first = row["name"].split(", ")
            writer.writerow({'first': first, 'last': last, 'house': row["house"]})

except FileNotFoundError:
    sys.exit(f"Could not read {input_file}")
