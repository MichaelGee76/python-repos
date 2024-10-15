import re


def main():
    name = input("Name: ").strip()
    pattern = re.search(r"^[a-zA-Z]\w{2,14}$", name)
    if pattern:
        print("Passt")
    else:
        print("Nope")


if __name__ == "__main__":
    main()
