def main():
    # i = 3
    # while i != 0:
    #     print("meow")
    #     i -= 1

    #  this code is poorly designed. If you would like to do a million iterations, you'd put a million numbers in that list. so the better way is to use the range function
    # for i in [0, 1, 2]:
    #     print("meow")

    for _ in range(
        3
    ):  # we do not need the variable name, that's why we can replace it by an underscore
        print("meow")
    print("I'm done!")
    print("meow\n" * 3, end="")


main()
