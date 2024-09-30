import random as ran


def main():
    while True:
        level = int(input("Level: "))
        if level not in range(1, 4):
            continue
        break

    if level == 1:
        problems = create_math_problems(1)
    elif level == 2:
        problems = create_math_problems(2)
    elif level == 3:
        problems = create_math_problems(3)

    print(problems[])


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
