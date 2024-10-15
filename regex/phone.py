import re


def main():
    number = input("Number? ").strip()

    pattern = re.search(r"^\d{3}-\d{3}-\d{4}$", number)

    if pattern:
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
