def main():
    # print_column(3)
    # print_row(4)
    print_square(3)


def print_column(height):
    for _ in range(height):
        print("#")


def print_row(width):
    print("?" * width)


def print_square(side):
    for i in range(side):
        for j in range(side):
            print("# ", end="")
        print()


if __name__ == "__main__":
    main()
