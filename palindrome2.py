def main():
    usr_input = input("Check palindrome: ").strip().replace(" ", "").lower()
    # reverse string
    reversed_usr_input = usr_input[::-1]

    if usr_input == reversed_usr_input:
        print("It's a palindrom.")
    else:
        print("It's not a palindrome")


if __name__ == "__main__":
    main()
