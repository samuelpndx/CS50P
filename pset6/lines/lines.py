import sys


def main():
    check_arguments(sys.argv)
    file_name = check_py_file(sys.argv)
    print(count_lines(file_name))


def check_arguments(arguments):
    if len(arguments) < 2:
        sys.exit("Too few command-line arguments")
    elif len(arguments) > 2:
        sys.exit("Too many command-line arguments")


def check_py_file(arguments):
    file_name = arguments[1]
    if file_name.split(".")[-1] == "py":
        return file_name
    else:
        sys.exit("Not a Python file")


def count_lines(file_name):
    try:
        with open(file_name) as file:
            count = 0
            for line in file:
                if line.strip().startswith("#") or line.strip() == "":
                    pass
                else:
                    count += 1
            return count
    except FileNotFoundError:
        sys.exit("File does not exits")


if __name__ == "__main__":
    main()
