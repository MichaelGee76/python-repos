import csv


def main():

    students = []
    with open("students.csv") as file:
        # for line in file:
        # name, home = line.rstrip().split(",")
        # student = {"name": name, "home": home}
        # students.append(student)
        reader = csv.reader(file)
        for name, home in reader:
            students.append({"name": name, "home": home})

    for student in sorted(students, key=lambda student: student["name"]):
        print(f"{student['name']} is from{student['home']}")


if __name__ == "__main__":
    main()
