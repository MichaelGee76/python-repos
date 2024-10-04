def main():
    pass
    while True:
        try:
            answer = input("Fraction: ").strip()
            percentage = convert(answer)
            print(gauge(percentage))
            break
        except (ValueError, ZeroDivisionError):
            print("Invalid input.")


def convert(fraction):
    x, y = fraction.split("/")
    x, y = int(x), int(y)
    if y == 0:
        raise ZeroDivisionError
    if x > y:
        raise ValueError
    fuel = round((x / y) * 100)
    return fuel


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
