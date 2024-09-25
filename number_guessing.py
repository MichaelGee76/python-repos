import random


def main():
    is_game = True
    while is_game:
        try:
            usr_number = int(
                input("Choose difficulty by typing a number between 1 and 100: ")
            )

        except ValueError:
            continue

        if usr_number > 100 or usr_number <= 0:
            print("Please read the instructions carefully and try again.")
            return
        # game logic
        random_number = get_random_number(usr_number)
        count = 1
        while True:

            guess = int(input("Guess: "))
            if guess == random_number:
                print(
                    f"{guess} is correct. You just needed {count} guess(es) to find the number."
                )
                break
            else:
                count += 1
                continue
        # repeat game interaction
        repeat = input("Play again? Yes/No: ").lower()

        if repeat.startswith("n"):
            is_game = False
        else:
            print("Ok then, let's play again.")


def get_random_number(n):
    return random.randint(1, n)


if __name__ == "__main__":
    main()
