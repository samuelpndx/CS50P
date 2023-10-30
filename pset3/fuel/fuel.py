def main():
    print(get_frac("Fraction: "))


def get_frac(prompt):
    while True:
        try:
            x, y = input(prompt).split(sep="/")
            percent = round(int(x) / int(y) * 100)
            if percent <= 100:
                if percent >= 99:
                    return "F"
                elif percent <= 1:
                    return "E"
                else:
                    return str(percent) + "%"
        except (ValueError, ZeroDivisionError):
            pass


main()
