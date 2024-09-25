import sys


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few args")
    elif len(sys.argv) > 2:
        sys.exit("Too many args")

    print("Hello, my name is", sys.argv[1])


if __name__ == "__main__":
    main()
