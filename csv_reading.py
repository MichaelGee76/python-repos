import csv


def main():
    with open("before.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            name, house = row
            print(f"Name {name}, House: {house}")


if __name__ == "__main__":
    main()
