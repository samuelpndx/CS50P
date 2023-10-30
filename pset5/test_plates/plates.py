def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not req_valid_size(s):
        return False
    elif not req_only_letters_numbers(s):
        return False
    elif not req_start_two_letters(s):
        return False
    elif not req_number_middle(s):
        return False
    else:
        return True


def req_valid_size(s):
    if 2 <= len(s) <= 6:
        return True
    return False


def req_only_letters_numbers(s):
    if s.isalnum():
        return True
    return False


def req_start_two_letters(s):
    if s[0:2].isalpha():
        return True
    return False


def req_number_middle(s):
    i=2
    for i in range(len(s)):
        if s[i].isdigit():
            if s[i] == "0":
                return False
            else:
                if s[i:].isdigit():
                    return True
    return True



if __name__ == "__main__":
    main()