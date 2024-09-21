def main():
    fruits = {
        "Apple": 130,
        "Avocado": 50,
        "Banana": 110,
        "Cantaloupe": 50,
        "Grapefruit": 60,
        "Grapes": 90,
        "Honeydew Melon": 50,
        "Kiwifruit": 90,
        "Lemon": 15,
        "Lime": 20,
        "Nectarine": 60,
        "Orange": 80,
        "Peach": 60,
        "Pear": 100,
        "Pineapple": 50,
        "Plums": 70,
        "Strawberries": 50,
        "Sweet Cherries": 100,
        "Tangerine": 50,
        "Watermelon": 80,
    }
    # strip() removes whitespaces and title() capitalzes every word
    item = input("Fruit: ").strip().title()
    # check if item is in dict and if so, use the item as the key and print out the calory
    if item in fruits:
        print(f"Calories: {fruits[item]}")


if __name__ == "__main__":
    main()
