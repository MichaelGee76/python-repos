import sys


def main():
    if len(sys.argv) != 2:
        sys.exit("Please provide argument")
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a valid python file")
    try:
        with open(sys.argv[1], "r") as file:
            count = 0
            for line in file.readlines():
                stripped_line = line.lstrip()
                if not stripped_line.startswith("#") and not stripped_line == "":
                    count += 1
            print(count)
    except FileNotFoundError:
        sys.exit("File not found")


if __name__ == "__main__":
    main()
