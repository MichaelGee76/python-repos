def main():
    usr_input = int(input("Type a year: "))
    print(f"{usr_input} is {is_leap(usr_input)}")


def is_leap(year):

    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


if __name__ == "__main__":
    main()
