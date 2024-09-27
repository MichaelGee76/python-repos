from collections import Counter
import string


def main():
    usr_input = input("Type a sentence. I'll count the words: ").strip().lower()
    usr_input = usr_input.translate(str.maketrans("", "", string.punctuation))
    usr_input = usr_input.split()

    counted = dict(Counter(usr_input))
    for key, value in counted.items():
        print(f"The word: '{key}' exists {value} times.")


if __name__ == "__main__":
    main()
