def main():
    usr_input = int(input("Generate fibonacci: "))
    print(f"The {usr_input}-th Fibonacci Number is {fibonacci(usr_input)}")


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b


if __name__ == "__main__":
    main()
