def hello(name="world"):
  print(f"Hello", name, end="!")
# capitalize userName and remove whitespace 
hello()
userName = input("What is your name? ").strip().capitalize()
hello(userName)  