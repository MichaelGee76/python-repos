import re


def main():
    email = input("What's your email? ").strip()
    # Das 'r' bedeutet raw string und verhindert, dass Python den backslash als escape char interpretiert
    if re.search(r"^[.+]@.+\.edu$", email):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
