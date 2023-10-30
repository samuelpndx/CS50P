import datetime
import re
import sys
import inflect

def main():
    p = inflect.engine()
    born_date = get_born_date()
    minutes = convert_to_minutes(born_date)

    print((p.number_to_words(minutes, andword="")).capitalize() + " minutes")


def get_born_date():
    return input("Date of Birth: ")


def convert_to_minutes(born_date):
    regex = "([0-9]{4})-([0-9]{2})-([0-9]{2})"
    try:
        if matches := re.search(regex, born_date):
            born_date = datetime.date(int(matches.group(1)), int(matches.group(2)), int(matches.group(3)))
        else:
            sys.exit("Invalid date")
    except (ValueError):
        sys.exit("Invalid date")

    return (datetime.date.today() - born_date).days*24*60


if __name__ == "__main__":
    main()