import re


def main():
    url = input("url: ").strip()
    pattern = re.search(r"^(http|https)://[a-z-]+\.[a-z]{2,3}$", url)
    if pattern:
        print("yes")
    else:
        print("no")


if __name__ == "__main__":
    main()
