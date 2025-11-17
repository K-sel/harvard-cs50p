months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    try:
        date = input("Date: ").strip()

        if "/" in date:
            month, day, year = date.split("/")
            month = int(month)
            day = int(day)
            year = int(year)

            # Validation
            if month < 1 or month > 12:
                raise ValueError
            if day < 1 or day > 31:
                raise ValueError

            print(f"{year}-{month:02d}-{day:02d}")
            break

        else:
            if "," not in date:
                raise ValueError

            parts = date.split(" ")
            if len(parts) != 3:
                raise ValueError

            month_name = parts[0].capitalize()
            day_str = parts[1].replace(",", "")
            year = int(parts[2])

            if month_name not in months:
                raise ValueError

            month = months.index(month_name) + 1
            day = int(day_str)

            # Validation
            if day < 1 or day > 31:
                raise ValueError

            print(f"{year}-{month:02d}-{day:02d}")
            break

    except (ValueError, IndexError):
        pass
