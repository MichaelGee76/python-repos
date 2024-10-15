import re


def main():
    email = input("Email: ").strip()
    pattern = re.search(
        r"^[a-zA-Z]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*\.[a-z]{2,4}$", email
    )
    if pattern:
        print("yeah")
    else:
        print("nee nee")


if __name__ == "__main__":
    main()
