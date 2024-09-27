import sys
import time


def main():
    # print("Hello, ", sys.argv[1])
    # try:
    #     usr_value = sys.argv[1]
    #     time.sleep(0.3)
    #     print(f"Hello, {usr_value}. How is your day?")
    # except IndexError:
    #     print("Please provide the missing argument")

    if len(sys.argv) < 2:
        sys.exit(("Too few arguments"))
    elif len(sys.argv) > 2:
        sys.exit(("Too many arguments"))

    else:
        print("Hello, my name is", sys.argv[1])
        time.sleep(3)
        print("I am the operator here")


if __name__ == "__main__":
    main()
