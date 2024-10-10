import sys
import csv


def main():
    if len(sys.argv) != 3:
        sys.exit("Invalid amount of arguments")
    input_data = sys.argv[1]
    output_data = sys.argv[2]

    with open(input_data) as file:
        reader = csv.reader(file)
        next(reader)

        with open(output_data, "a") as output_file:
            writer = csv.writer(output_file)
            writer.writerow(["First_Name", "Last_Name", "House"])

            for line in reader:
                name = line[0]
                house = line[1]
                last_name, first_name = name.split(", ")

                writer.writerow([first_name, last_name, house])


if __name__ == "__main__":
    main()
