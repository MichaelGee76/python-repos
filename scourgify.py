import sys
import csv


def main():
    # check if 2 arguments wer passed
    if len(sys.argv) != 3:
        sys.exit("Invalid input")

    # set arguments to variables
    input_data = sys.argv[1]
    output_data = sys.argv[2]
    # # control if program is responding in the expected way
    # print(input_data, output_data)

    with open(input_data, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            name, house = row
            name = name.split(", ")

            if len(name) == 2:
                last_name = name[0].strip()
                first_name = name[1].strip()

            with open(output_data, "w") as file:
                


if __name__ == "__main__":
    main()
