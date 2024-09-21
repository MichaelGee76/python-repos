def main():
    # print_square(4)
    print_square_easy(8)


def print_square(side):
    for i in range(side):
        for j in range(side):
            print("# ", end="")
        print()


def print_square_easy(side):
    for i in range(side):
        print("# " * side)


if __name__ == "__main__":
    main()
