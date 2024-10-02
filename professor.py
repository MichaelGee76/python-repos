import random as ran


def main():
    while True:
        try:
            level = int(input("Level: "))
            if level not in range(1, 4):
                continue
            break
        except ValueError:
            continue

    is_correct = 0
    if level == 1:
        problems = create_math_problems(1)
    elif level == 2:
        problems = create_math_problems(2)
    elif level == 3:
        problems = create_math_problems(3)
    for problem, result in problems.items():

        counter = 0
        while counter < 3:
            try:
                answer = int(input(f"{problem} = "))
                if answer != result:
                    print("EEE")
                    counter += 1
                    continue
                if answer == result:
                    is_correct += 1
                    break

            except ValueError:
                print("EEE")
                counter += 1
                continue

        if counter == 3:
            print(f"{problem} = {result}")

    if is_correct > 5:
        print(f"Congrats, you answered {is_correct} questions right!")
    if is_correct <= 5:
        print(f"Not bad, you answered {is_correct} questions right!")
    if is_correct == 0:
        print(f"{is_correct} correct answers were given. You got this, just try again.")


def create_math_problems(n):
    math_problems = {}

    if n == 1:
        for i in range(10):
            x = ran.randint(1, 10)
            y = ran.randint(1, 10)
            addition_key = f"{x} + {y}"
            addition_value = x + y
            math_problems[addition_key] = addition_value
        return math_problems
    elif n == 2:
        for i in range(10):
            x = ran.randint(10, 99)
            y = ran.randint(10, 99)
            addition_key = f"{x} + {y}"
            addition_value = x + y
            math_problems[addition_key] = addition_value
        return math_problems
    elif n == 3:
        for i in range(10):
            x = ran.randint(100, 999)
            y = ran.randint(10, 999)
            addition_key = f"{x} + {y}"
            addition_value = x + y
            math_problems[addition_key] = addition_value
        return math_problems


if __name__ == "__main__":
    main()
