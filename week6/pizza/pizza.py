from tabulate import tabulate
import csv, sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

filename = sys.argv[1]
if filename.split(".")[1] != "csv":
    sys.exit("Not a CSV file")

with open(filename) as file:
    reader = csv.DictReader(file)
    table = []
    for row in reader:
        table.append(row)

    print(tabulate(table, headers="keys", tablefmt="grid"))
