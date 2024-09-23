def main():
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00,
    }
    order = []
    total = 0
    while True:
        try:
            item = input("Item: ").strip().title()
            order.append(item)
            total += menu[item]
            print(f"Total: ${total:.2f}")

        except EOFError:
            return
        except KeyError:
            continue


if __name__ == "__main__":
    main()
