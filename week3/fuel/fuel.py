def main():
    fuel = prompt_user()
    pct = round(fuel * 100)

    if pct <= 1:
        print("E")
    elif pct >= 99:
        print("F")
    else:
        print(f"{pct}%")


def prompt_user():
    while True:
        try:
            val = input("Fraction: ")
            a, b = val.split("/")
            div = int(a) / int(b)
            if div > 1 or div < 0 :
                raise ValueError
            else:
                return div
        except (ValueError, ZeroDivisionError):
            pass

main()
