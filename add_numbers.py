def main():
    numbers = input("Type some numbers: ").split()

    print(sum_numbers(numbers))


def sum_numbers(number_list):
    result = 0
    for number in number_list:
        result += int(number)

    return f"Result: {result}"


if __name__ == "__main__":
    main()
