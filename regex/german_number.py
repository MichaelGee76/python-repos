import re


def main():
    number = input("Number: ").strip()
    pattern = re.search(r"^(\+49|0049|0)[1-9]\d{1,4} \d{3,10}(-\d{1,4})?$", number)
    if pattern:
        print("Yes")
    else:
        print("Nope")


if __name__ == "__main__":
    main()
