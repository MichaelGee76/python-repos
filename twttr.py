# ask the user for a phrase
# print out the phrase again, but remove vowels(A, E, I, O, U)


def main():
    vowels = ["a", "e", "i", "o", "u", "A", "E" "I", "O", "U"]

    phrase = input("Input: ")
    formatted_phrase = ""
    for char in phrase:
        if char in vowels:
            char.replace(char, "")
        else:
            formatted_phrase += char
    print(formatted_phrase)


if __name__ == "__main__":
    main()
