import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = "^(1[0-2]|[0-9]):?([0-5][0-9])? (AM|PM) to (1[0-2]|[0-9]):?([0-5][0-9])? (AM|PM)$"
    if matches := re.search(pattern, s):
        arrival = new_time(matches.group(1), matches.group(2), matches.group(3))
        departure = new_time(matches.group(4), matches.group(5), matches.group(6))
        return f"{arrival} to {departure}"
    else:
        raise ValueError


def new_time(hour, minute, am_pm):
    if int(hour) > 12:
        raise ValueError

    if am_pm == "AM":
        if hour == "12":
            hour = 0
        else:
            hour = int(hour)
    else:
        if hour == "12":
            hour = int(hour)
        else:
            hour = int(hour) + 12

    if minute == None:
        minute = 0
    else:
        minute = int(minute)

    return f"{hour:02d}:{minute:02d}"


if __name__ == "__main__":
    main()
