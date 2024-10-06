def main():
    with open("names.txt", "r") as file:
        #     lines = file.readlines()
        # for line in lines:
        #     print("Hello, ", line.rstrip())  # rstrip() has the same effect line end=""
        for line in sorted(
            file, reverse=False
        ):  # sorted(file) outputs ascending, reverse=reversed outputs descendings
            print("hello,", line.rstrip())


if __name__ == "__main__":
    main()
