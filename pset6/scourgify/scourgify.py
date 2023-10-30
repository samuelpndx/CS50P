import sys
import csv


def main():
    check_arguments(sys.argv)
    table = scourgify(sys.argv[1])
    new_file(table, sys.argv[2])

def check_arguments(arguments):
    if len(arguments) < 3:
        sys.exit("Too few command-line arguments")
    elif len(arguments) > 3:
        sys.exit("Too many command-line arguments")


def scourgify(before):
    table = []
    try:
         with open(before) as file:
             reader = csv.DictReader(file)
             for row in reader:
                 last, first = row["name"].split(", ")
                 table.append({"first": first, "last": last, "house": row["house"]})
             return table

    except FileNotFoundError:
         sys.exit("Could not read invalid_file.csv")

def new_file(table, file_name):
    with open(file_name, "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for dict in table:
            writer.writerow(dict)


if __name__ == "__main__":
     main()
