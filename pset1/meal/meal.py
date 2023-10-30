def main():
    now = convert(input("What time is it? "))
    if 7 <= now <= 8:
        print("breakfast time")
    elif 12 <= now <= 13:
        print("lunch time")
    elif 18 <= now <= 19:
        print("dinner time")


def convert(time):
    hour, minute = time.split(":")
    if minute.endswith("a.m."):
        minute = minute.removesuffix(" a.m.")
        newtime = float(hour) + (float(minute) / 60.0)
    elif minute.endswith("p.m."):
        minute = minute.removesuffix(" p.m.")
        newtime = (float(hour) + 12) + (float(minute) / 60.0)
    else:
        newtime = float(hour) + (float(minute) / 60.0)

    return newtime


if __name__ == "__main__":
    main()
