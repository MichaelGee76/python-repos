import sys
import os
import json


def main():
    while True:
        try:
            choice = int(
                input(
                    "Choose an option:\n1: create contact\n2: show contacts\n3: delete contact\n4: search contact\n5: end program\n"
                )
            )
        except ValueError:
            sys.exit("Invalid input")
        if choice == 5:
            sys.exit("Goodbye, see you next time")

        if not os.path.exists("contacts"):
            os.makedirs("contacts")  # Erstellt den Ordner, wenn er nicht existiert
        if not os.path.exists("contacts/contact.json"):
            create_dict()

        open_dict(choice)


def create_dict():
    with open("contacts/contact.json", "w") as file:
        json.dump({}, file)  # Speichert ein leeres Wörterbuch
    print("contact.json successfully created")


def open_dict(n):
    with open("contacts/contact.json", "r+") as file:
        if n == 1:
            create_contact()
        elif n == 2:
            show_contact()
        elif n == 3:
            delete_contact()
        elif n == 4:
            search_contact()


def show_contact():
    with open("contacts/contact.json", "r") as file:
        content = json.load(file)
        if content:
            for name, number in content.items():
                print(f"Name: {name}, Number: {number}")
        else:
            print("No contacts available")


def create_contact():
    name = input("Enter name: ")
    number = input("Enter phone number: ")
    with open("contacts/contact.json", "r+") as file:
        content = json.load(file)
        content[name] = number
        file.seek(0)
        json.dump(content, file)
        file.truncate()
    print(f"Contact {name} successfully added")


def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    with open("contacts/contact.json", "r+") as file:
        content = json.load(file)
        if name in content:
            del content[name]
            file.seek(0)
            json.dump(content, file)
            file.truncate()
            print(f"Contact {name} deleted")
        else:
            print(f"Contact {name} not found")


def search_contact():
    name = input("Enter the name to search: ")
    with open("contacts/contact.json", "r") as file:
        content = json.load(file)
        if name in content:
            print(f"Found contact: {name}, Number: {content[name]}")
        else:
            print(f"Contact {name} not found")


if __name__ == "__main__":
    main()
