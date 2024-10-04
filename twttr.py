# ask the user for a phrase
# print out the phrase again, but remove vowels(A, E, I, O, U)


def main():

    phrase = input("Input: ")
    print(shorten(phrase))


def shorten(word):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    formatted_phrase = ""
    for char in word:
        if char in vowels:
            char.replace(char, "")
        else:
            formatted_phrase += char
    return formatted_phrase


if __name__ == "__main__":
    main()
