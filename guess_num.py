import random as ran


def guessing_game():
    is_game = True
    counter = 0
    random_number = ran.randint(1, 100)
    print("I think about a number between 1 and 100.")

    while is_game:

        guess = int(input("Guess my number: "))
        counter += 1
        if guess == random_number:
            print(f"{guess} is correct. It took {counter} tries to find the number.")
            return counter
        else:
            if guess < random_number:
                print("My number is higher.")
            else:
                print("My number is lower.")
        if counter == 10:
            print(f"Sorry, {random_number} was my number.")
            is_game = False
            return -1


def main():
    guessing_game()


if __name__ == "__main__":
    main()
