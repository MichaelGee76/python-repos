import re


def main():
    password = input("Password: ").strip()
    """
    password muss min 8 zeichen lang sein
    mindestens einen Großbuchstaben
    mindesten eine Ziffer
    kann Sonderzeichen @, #, $, % enthalten
    """
    pattern = re.search(r"^(?=.*[A-Z])(?=.*\d)[A-Za-z\d@#$%]{8,}$", password)
    if pattern:
        print("yes")
    else:
        print("no")


if __name__ == "__main__":
    main()
