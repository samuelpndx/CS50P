import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    ip_pattern = "^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$"
    if  re.search(ip_pattern, ip):
        return True
    else:
        return False


if __name__ == "__main__":
    main()

