# def main() in main we call get_number() and set its value to number
# we call meow(number) with the parameter number


def main():
    number = get_number()
    meow(number)


# in get_number() we ask the user for n. until n is greater than 0 we keep asking. that doesn't allow the user to type in negative number or zero. when we receive a number we can work with i.e. 1 or greater, then we return n


def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n


# meow(n) needs a parameter n, when we call meow(n) than we run our for loop and print "meow"  n times


def meow(n):
    for _ in range(n):
        print("meow")


if __name__ == "__main__":
    main()
