list = []

while True:
    try:
        item = input("")
        list.append(item)
    except (EOFError, KeyError):
            break

groceries = set(list)
groceries = sorted(groceries)

for item in groceries:
    print(f"{list.count(item)} {str(item).upper()}")


