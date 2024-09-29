def main():
    names_list = []
    collect_name = True
    while collect_name:
        try:
            names_list.append(input("Name: "))

        except EOFError:
            break
    prefix = "Adieu, adieu, to"
    # if just one name
    if len(names_list) == 1:
        names_list = "".join(names_list)
        print(prefix, names_list)
    # if two names
    elif len(names_list) == 2:
        print(f"{prefix} {names_list[0]} and {names_list[1]}")
    # if 3 or more names
    elif len(names_list) > 2:
        temp_list = []
        for name in names_list[:-1]:
            temp_list.append(name + ", ")
        print(f"{prefix} {"".join(temp_list)}and {names_list[-1]}")


if __name__ == "__main__":
    main()
