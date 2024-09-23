def main():
    grocery_list = []
    while True:
        try:
            item = input()
            grocery_list.append(item)
        except EOFError:
            break

    for i in range(len(grocery_list)):
        grocery_list[i] = grocery_list[i].upper()

    output_list(grocery_list)


def output_list(list):
    # count values
    grocery_dict = {i: list.count(i) for i in list}
    # sort alphabetically
    sorted_grocery_dict = dict(sorted(grocery_dict.items()))
    for key, value in sorted_grocery_dict.items():
        print(f"{value} {key}")


if __name__ == "__main__":
    main()
