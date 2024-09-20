def main():
    students = ["Hermione", "Harry", "Ron"]
    # print("Last: ", students[-1].upper())
    # for item in list, good way to print out list items
    for student in students:
        print(student)
    print("###################")
    for i in range(len(students)):
        print(i + 1, students[i])


if __name__ == "__main__":
    main()
