def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percent = convert(fraction)
            print(gauge(percent))
            break
        except (ValueError, ZeroDivisionError):
            pass


def convert(fraction):
    x, y = fraction.split(sep="/")

    percent = round(int(x) / int(y) * 100)

    if int(x) > int(y):
        raise ValueError
    
    return percent


def gauge(percentage):
    if percentage <= 100:
        if percentage >= 99:
            return "F"
        elif percentage <= 1:
            return "E"
        else:
            return str(percentage) + "%"


if __name__ == "__main__":
    main()
