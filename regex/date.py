import re


def main():
    date = input("Date: ")
    # date format DD/MM/YYYY
    pattern = re.search(r"^(0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1[0-2])\/\d{4}$", date)
    if pattern:
        print("Yes")
    else:
        print("no")


if __name__ == "__main__":
    main()
