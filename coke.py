# my approach:

# def main():
#     # ask user to insert a coin to buy a coke for 50 cents
#     # when coin is inserted print out how much is left
#     # when user inserted at least 50 cent print out how much is the change

#     coins = 0
#     cost = 50
#     accepted_coins = [25, 10, 5]

#     while coins < cost:
#         inserted_coins = int(input("Insert Coin: "))
#         if inserted_coins in accepted_coins:
#             coins += inserted_coins
#         if cost - coins == 0:
#             print("Change Owed:", 0)
#             return
#         else:
#             if cost - coins < 0:
#                 print("Change Owed:", (cost - coins) * -1)
#             else:
#                 print("Amount Due:", cost - coins)


# if __name__ == "__main__":
#     main()

# not my approach:(((())))


def main():
    coins = 0
    cost = 50
    accepted_coins = [25, 10, 5]

    while coins < cost:
        inserted_coins = int(input("Insert Coin: "))
        if inserted_coins in accepted_coins:
            coins += inserted_coins
        if coins < cost:
            print(f"Amount Due: {cost - coins}")

    # Nach der Schleife, wenn coins >= cost ist
    print(f"Change Owed: {coins - cost}")


if __name__ == "__main__":
    main()
