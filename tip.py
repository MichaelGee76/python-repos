# def main():
#     dollars = dollars_to_float(input("How much was the meal? "))
#     percent = percent_to_float(input("What percentage would you like to tip? "))
#     tip = dollars * percent
#     print(f"Leave ${tip:.2f}")


# def dollars_to_float(d):
#     return round(float(d), 2)


# def percent_to_float(p):
#     # TODO


# main()

u = input("How much: ")


new_u = u.replace("$", "")
print(round(float(new_u), 2))

p = input("How much percent: ")
new_p = p.replace("%", "")
print(round(float(new_p), 2)/100)


