def main():

    forbidden_vowels = [
        "a",
        "e",
        "i",
        "o",
        "u",
        "A",
        "E",
        "I",
        "O",
    ]

    usr_input = input("Type something: ")
    formatted = ""
    for char in usr_input:
        if char not in forbidden_vowels:
            formatted += char

    print(formatted)


if __name__ == "__main__":
    main()
