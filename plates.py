"""
“All vanity plates must start with at least two letters.”
“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
“No periods, spaces, or punctuation marks are allowed.”

"""


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # in range of min 2 and max 6
    if len(s) not in range(2, 7):
        return False
    # check if only numbers or letters
    elif not s.isalnum():
        return False
    # check if first two char are alphabetic
    elif not s[0:2].isalpha():
        return False

    for i in range(len(s)):
        # check for number if number is 0 return false
        if s[i].isdigit():
            if s[i] == "0":
                return False
            # start with 2. for loop to check if after the founded number is a letter(which is not allowed)
            for j in range(i, len(s)):
                if s[j].isalpha():
                    return False
                # if we reach this part of code, it means there was no letter after the first found number. That means, we finished to check everything and we escape by break
            break
        # if we passed all conditions, we return True to main()
    return True


if __name__ == "__main__":
    main()
