def main():
    while True:
        try:
            answer = input("Fraction: ").strip()
            x, y = answer.split("/")
            x, y = int(x), int(y)
            fuel = round((x / y) * 100)
            print(f"{fuel}%")
            break

        except (ValueError, ZeroDivisionError):
            continue


if __name__ == "__main__":
    main()
