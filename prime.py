def main():

    usr_input = int(input("Is prime? "))
    print(is_prime(usr_input))


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return "Not a prime number "

    else:
        return "It's a prime"


if __name__ == "__main__":
    main()
