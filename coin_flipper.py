import random as ran
import statistics


def main():
    # coin = ran.choice(["heads", "tails", "side"])
    # print(coin)

    # number = ran.randint(1, 10)
    # print(number)

    # my_list = [
    #     "Queen",
    #     "Jack",
    #     "King",
    #     "Ace",
    #     "2",
    #     "3",
    #     "4",
    #     "5",
    #     "6",
    #     "7",
    #     "8",
    #     "9",
    #     "10",
    # ]
    # print(my_list)
    # print("-----------------------------")
    # ran.shuffle(my_list)
    # for i in my_list:
    #     print(i)
    # print(my_list)
    # shuffled = ran.shuffle(my_list)
    # print(shuffled)
    summed = []
    for i in range(50):
        summed.append((round(ran.triangular(1, 10, 4), 2)))
    print(statistics.mean(summed))


if __name__ == "__main__":
    main()
