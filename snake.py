def main():

    camel_case = input("Type a camelCase word: ")
    convert_cc_to_sc(camel_case)


def convert_cc_to_sc(word):
    temp = ""
    for i in word:
        if i.isupper():
            temp += "_" + i.lower()
        else:
            temp += i
    # snake_cased = temp.replace(" ", "_")
    print(temp)


main()
