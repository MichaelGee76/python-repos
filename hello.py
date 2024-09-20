# ask user for their name
userName = input("What's your name? ")
# say hello to user
# print("Hello ", end="")
# print(userName, end="!")

# remove whitespace from input string and capitalize the first letter
userName = userName.strip().capitalize()
# capitalize all firt letters
userName = userName.title()
# using f string
# print(f"Hello {userName}!")

# spit users name into first and last name
first, last = userName.split(" ")
first.capitalize()
print(f"Hello {first}!")



