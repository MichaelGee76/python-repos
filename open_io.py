def main():
    f = open("test.txt", "w", encoding="utf8")
    f.write("Fisher men, fishers bloopers. Find no gold.")
    x = f.read()
    print(x)


if __name__ == "__main__":
    main()
