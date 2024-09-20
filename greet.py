def greet(input):
  
  if "hello" in input:
    return "hello, there"
  else:
    return "who the heck are you?"

greeting = greet("hello hello hello")

# when return a value AND store in a variable, I am able to modify the return value, as I want. i.e. capitalize it, title it, add or remove something

print(greeting.title() + " " + input("What is your name? "), end="!")

lastword = greeting

print("This is my last words to you: ", lastword)