import random as ran


def main():
    while True:
        try:
            level = int(input("Level: "))
            if level < 1:
                continue
            break
        except:
            continue
    random_number = ran.randint(1, level)
    while True:
        try:
            usr_guess = int(input("Guess: "))
        except:
            continue
        if usr_guess < random_number:
            print("Too small!")
            continue
        elif usr_guess > random_number:
            print("Too large!")
            continue
        else:
            print("Just right!")
            return


if __name__ == "__main__":
    main()
