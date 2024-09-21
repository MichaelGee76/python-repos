def main():
    students = {
        "Hermione": "Griffindor",
        "Harry": "Griffindor",
        "Ron": "Griffindor",
        "Draco": "Slytherin",
    }
    for student in students:
        print(student, students[student], sep=" lives in: ")


if __name__ == "__main__":
    main()
