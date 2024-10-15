import re


def main():
    name = input("Name: ").strip()
    pattern = re.search(r"^[a-zA-Z]+$")
    if pattern:
        print("Ok")
    else:
        print("not ok")


if __name__ == "__main__":
    main()
