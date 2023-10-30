from tabulate import tabulate
import sys
import csv


def main():
    check_arguments(sys.argv)
    file_name = check_csv_file(sys.argv)
    table = format_table(file_name)

    print((tabulate(table, headers="firstrow", tablefmt="grid")))


def check_arguments(arguments):
    if len(arguments) < 2:
        sys.exit("Too few command-line arguments")
    elif len(arguments) > 2:
        sys.exit("Too many command-line arguments")


def check_csv_file(arguments):
    file_name = arguments[1]
    if file_name.split(".")[-1] == "csv":
        return file_name
    else:
        sys.exit("Not a CSV file")


def format_table(file_name):
    table = []
    try:
         with open(file_name) as file:
             reader = csv.reader(file)
             for row in reader:
                 table.append(row)
             return table

    except FileNotFoundError:
         sys.exit("File does not exists")


if __name__ == "__main__":
     main()
