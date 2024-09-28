import cowsay
import sys


def main():
    if len(sys.argv) == 2:
        cowsay.trex("Hello," + sys.argv[1])


if __name__ == "__main__":
    main()
