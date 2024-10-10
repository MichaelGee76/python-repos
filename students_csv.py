# with open("students.csv") as file:
#     for line in file:
#         row = line.rstrip().split(", ")
#         print(f"{row[0]} lives in {row[1]}")

# students = []

# with open("students.csv") as file:
#     for line in sorted(file):
#         name, house = line.rstrip().split(", ")
#         # print(f"{name} lives in {house}")
#         student = {}
#         student["name"] = name
#         student("house") = house
#         students.append(student)
# for student in students:
#     print(f"{student['name']} lives in {house['house']}")

# students = []

# with open("students.csv") as file:
#     for line in file:
#         name, home = line.rstrip().split(", ")
#         student = {"name": name, "home": home}
#         students.append(student)


# # def get_name(student):
# #     return student["name"]

# # lambda functions können anonym aufgerufen werden und ersetzen eine ausgelagerte funktion


# for student in sorted(students, key=lambda student: student["home"]):
#     print(f"{student['name']} from {student['home']}")

#


import csv

students = []

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")
