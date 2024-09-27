def main():
    usr_input = int(input("Type a number: "))
    for i in range(1, usr_input + 1):
        print(f"{i}" * i)


if __name__ == "__main__":
    main()
