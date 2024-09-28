import sys


def main():
    # start iterating from 1. index
    for arg in sys.argv[1:]:
        print("hell, O my name is", arg)


if __name__ == "__main__":
    main()
