import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    match = re.fullmatch(
        r"(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)",
        s
    )
    if not match:
        raise ValueError("Invalid format")

    h1, m1, period1, h2, m2, period2 = match.groups()
    h1, h2 = int(h1), int(h2)
    m1 = int(m1) if m1 else 0
    m2 = int(m2) if m2 else 0

    if not (0 <= m1 <= 59 and 0 <= m2 <= 59):
        raise ValueError
    if not (1 <= h1 <= 12 and 1 <= h2 <= 12):
        raise ValueError

    h1 = to24(h1, m1, period1)
    h2 = to24(h2, m2, period2)

    return f"{h1:02}:{m1:02} to {h2:02}:{m2:02}"

def to24(h, m, period):
    if period == "AM":
        return 0 if h == 12 else h
    else:
        return 12 if h == 12 else h + 12

if __name__ == "__main__":
    main()
