def main():
    greeting = input("Greeting: ")

    print(f"${value(greeting)}")


def value(greeting):
    greeting = clean_text(greeting)
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


def clean_text(text):
    return text.strip().lower()


if __name__ == "__main__":
    main()