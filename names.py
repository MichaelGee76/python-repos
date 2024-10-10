# def main():
#     name = input("What's your name? ")

#     file = open("names.txt", "a")
#     file.write(f"{name}\n")
#     file.close()


# if __name__ == "__main__":
#     main()

# for _ in range(3):
#     name = input("What's your name? ").strip()

#     with open("my_name_file.txt", "a") as file:
#         file.write(f"{name}\n")

# with open("my_name_file.txt", "r") as file:
#     lines = file.readlines()

# for line in lines:
#     print(f"Hello, {line}", end="")

# print(type(file))

# with open("my_name_file.txt", "r") as file:
#     for line in sorted(file):
#         print("hello,", line.rstrip())

names = []

with open("my_name_file.txt") as file:
    for line in file:
        names.append(line.rstrip())
count = 1
for name in sorted(names):
    name = f"student#{count}"
    count += 1
    print(name)
