import sys
import csv


def main():
    if len(sys.argv) != 3:
        sys.exit("Invalid amount of arguments")
    input_data = sys.argv[1]
    output_data = sys.argv[2]

    try:
        with open(input_data) as file:
            reader = csv.reader(file)
            next(reader)

            with open(output_data, "w") as output_file:
                writer = csv.writer(output_file)
                writer.writerow(["first", "last", "house"])

                for line in reader:
                    name = line[0]
                    house = line[1]
                    last_name, first_name = name.split(", ")

                    writer.writerow([first_name, last_name, house])
    except FileNotFoundError:
        sys.exit(f"Could not read {input_data}")


if __name__ == "__main__":
    main()
