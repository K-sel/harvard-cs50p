import inflect
import sys

p = inflect.engine()
names = []

while True:
    try:
        s = input("Name : ")
        if len(s) == 0:
            raise EOFError
        else:
            names.append(s.strip())
    except EOFError:
        print("\n")
        print(f"Adieu, adieu, to {p.join(names)}")
        sys.exit(0)
