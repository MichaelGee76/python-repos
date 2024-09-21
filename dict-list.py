def main():

    students = [
        {"name": "Hermione", "house": "Griffindor", "patronus": "Otter"},
        {"name": "Harry", "house": "Griffindor", "patronus": "Stag"},
        {"name": "Ron", "house": "Griffindor", "patronus": "Jack Russel Terrier"},
        {"name": "Draco", "house": "Slytherin", "patronus": None},
    ]

    for student in students:
        print(student["name"], student["house"], student["patronus"])


if __name__ == "__main__":
    main()
