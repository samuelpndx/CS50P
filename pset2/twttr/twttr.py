vowels = ["a", "e", "i", "o", "u"]

def main():
    text = input("Input: ")
    print("Output:", end="")
    for c in text:
        if not is_vowel(c):
            print(c, end = "")
    print()

def is_vowel(c):
    for v in vowels:
        if c == v  or c == v.upper():
            return True
    return False

main()

