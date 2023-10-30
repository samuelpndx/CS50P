def main():
    text = input("Input: ")
    print("Output:", shorten(text))


def shorten(word):
    shortened = ""
    for c in word:
        if not is_vowel(c):
            shortened += c
    return f"{shortened}"


def is_vowel(c):
    vowels = ["a", "e", "i", "o", "u"]

    for v in vowels:
        if c == v or c == v.upper():
            return True
    return False


if __name__ == "__main__":
    main()
