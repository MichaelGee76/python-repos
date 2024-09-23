import time


def main():
    count = 1
    print("Please enter an integer.")
    while True:
        try:
            x = input("What is X? ")
            if x == "What is X?":
                print(
                    "You shall not answer my question by another question. Self destruction sequence started\n\n"
                )

                for i in range(9, 0, -1):
                    print(i, ". . .")
                    time.sleep(1)
                print_new_line(100)
                time.sleep(3)
                print("Boom")
                print_new_line(10)
                return
            x = int(x)
        except ValueError:
            print("X is not an integer.")
            count += 1
        else:
            break
    if x == 42:
        print(
            f"X is {x} The Answer to the Ultimate Question of Life, the Universe, and Everything \nYou just needed {count} tries to find it."
        )

    else:
        print(
            f"X is {x}. You just needed {count} tries to solve that simple problem of typing just an integer."
        )


def print_new_line(n):
    for i in range(n):
        print()


if __name__ == "__main__":
    main()
