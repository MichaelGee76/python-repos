def main():
    name = input("What's your name: ")
    with open("name.txt", "a") as file:
        file.write(f"{name}\n")


if __name__ == "__main__":
    main()
