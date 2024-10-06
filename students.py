def main():
    with open("students.csv") as file:
        for line in file:
            # row = line.rstrip().split(",")
            # print(f"{row[0]} lives in{row[1]}")
            name, house = line.rstrip().split(",")
            print(f"{name} lives in{house}")


if __name__ == "__main__":
    main()
