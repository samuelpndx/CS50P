def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    yyyy, mm, dd = convert_date(months, "Date: ")

    print(f"{(yyyy)}-{mm:02}-{dd:02}")


def convert_date(months, prompt):
    while True:
        try:
            date = input(prompt)
            if "/" in date:
                month, day, year = date.split(sep="/")
            elif "," in date:
                month, day, year = date.replace(",", "").split()
                month = months.index(month) + 1
            else:
                raise ValueError

            if 0 < int(day) < 32 and 0 < int(month) < 13:
                return int(year), int(month), int(day)

        except ValueError:
            pass


main()
