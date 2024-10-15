import re


def main():
    usr_str = input("String: ").strip()
    pattern = re.search(r"^[a-zA-Z]+$|^\d+$", usr_str)
    # alternativ
    # pattern = re.match(r"^([a-zA-Z]+|\d+)$") es geht aber beides. das auskommentierter ist wohl besser lesbar
    if pattern:
        print("Yes")
    else:
        print("Nö")


if __name__ == "__main__":
    main()
