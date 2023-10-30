import validators


def main():
    print(validate(input("What's yout email address? ")))


def validate(s):
    if validators.email(s):
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()
    