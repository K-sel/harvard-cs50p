import datetime as dt
import re
import inflect
import sys

p = inflect.engine()
pattern = r'^(\d{4})-(0[1-9]|1[0-2]|[1-9])-([1-9]|0[1-9]|[1-2]\d|3[0-1])$'


def main():
    birth = input("Date of Birth: ")
    year, month, day = get_birth(birth)

    dt_birth = dt.date(year, month, day)
    dt_now = dt.date.today()
    dt_delta = dt_now - dt_birth
    tot_seconds = int(dt_delta.total_seconds()/60)

    phrase = f"{p.number_to_words(tot_seconds, andword=" ")} minutes"
    print(phrase.capitalize())


def get_birth(birth):
    try:
        if matches := re.search(pattern, birth):
            year = matches.group(1)
            month = matches.group(2)
            day = matches.group(3)
            return int(year), int(month), int(day)
        else:
            raise ValueError
    except ValueError:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()
