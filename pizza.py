from tabulate import tabulate
import sys
import csv


def main():
    if len(sys.argv) != 2:
        sys.exit("Invalid Input")
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a valid csv")

    with open(sys.argv[1], "r") as file:

        reader = csv.DictReader(file)
        lines = []

        headers = reader.fieldnames

        lines.append(headers)

        for row in reader:

            line = []
            for header in headers:
                line.append(row[header])
            lines.append(line)

    print(tabulate(lines, headers="firstrow", tablefmt="grid"))


if __name__ == "__main__":
    main()
