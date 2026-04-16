import sys

loc_count = 0

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

filename = sys.argv[1]
if filename.split(".")[1] != "py":
    sys.exit("Not a Python file")


try:
    with open(filename, "r") as file:
        for line in file:
            if not line.strip().startswith("#") and line.lstrip():
                loc_count+=1

except FileNotFoundError:
    sys.exit("File does not exist")

print(loc_count)


