def main():
    usr_input = int(input("Type a number: "))

    for n in range(1, usr_input + 1):
        if is_prime(n):
            print("Prime", end=" ")
        if n % 3 == 0 and n % 5 == 0:
            print("FizzBuzz")
        elif n % 3 == 0:
            print("Fizz")
        elif n % 5 == 0:
            print("Buzz")

        else:
            print(n)


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    main()
