name= input("What's your name? ")

# if name == "Harry":
#   print("Gryffindor")
# elif name =="Hermione":
#   print("Gryffindor")
# elif name== "Ron":
#   print("Gryffindor")   
# elif name == "Draco":
#   print("Slytherin")
# else:
#   print("Who")  

# juist another approach
# if name == "Harry" or name == "Hermione" or name== "Ron":
#   print("Gryffindor")
# elif name == "Draco":
#   print("Slytherin")
# else:
#   print("Who")    

# another way to do is:

match name:
  case "Harry" | "Hermione" | "Ron":
    print("Gryffindor")
  case "Draco":
    print("Slytherin")
  case _: # underscore is a wild card to cover every other name
    print("Who?")
