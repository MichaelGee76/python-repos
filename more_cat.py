def main():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break  # break interrupts the while loop, regardless of the indedentation

    for _ in range(n):
        print("meow")


if __name__ == "__main__":
    main()
