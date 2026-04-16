def main():
    plate = input("Plate: ")
    print("Valid" if is_valid(plate) else "Invalid")


def is_valid(s):
    # Must be 2–6 chars
    if not (2 <= len(s) <= 6):
        return False
    # Must start with at least 2 letters
    if not s[:2].isalpha():
        return False
    # No punctuation or spaces allowed
    for c in s:
        if not (c.isalpha() or c.isdigit()):
            return False
    # Once a digit appears, no letters after
    first_digit = None
    for i, c in enumerate(s):
        if c.isdigit():
            if first_digit is None:
                first_digit = i
            if c == "0" and first_digit == i:
                # First digit cannot be 0
                return False
        else:
            if first_digit is not None:
                # Letter after a digit
                return False
    return True


if __name__ == "__main__":
    main()
