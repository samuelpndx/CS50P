import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = ".+src=\".+embed\/(.+?)\""
    if matches := re.search(pattern, s):
        return ("https://youtu.be/" + matches.group(1))
    else:
        return None


if __name__ == "__main__":
    main()