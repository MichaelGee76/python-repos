import random as ran


def main():
    level = get_level()
    correct_answers = 0
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        answer = x + y

        for _ in range(3):
            try:
                usr_input = int(input(f"{x} + {y} = "))
                if usr_input == answer:
                    correct_answers += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
                pass
    print(f"You answered {correct_answers} questions right.")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in range(1, 4):
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return ran.randint(1, 9)
    elif level == 2:
        return ran.randint(10, 99)
    elif level == 3:
        return ran.randint(100, 999)


if __name__ == "__main__":
    main()
