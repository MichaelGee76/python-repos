import random as ran


def main():
    cards = [i for i in range(1, 101)]
    ran.shuffle(cards)
    # for card in cards:
    #     print(card)
    print(cards)


if __name__ == "__main__":
    main()
