# For calculating we need to specify the data type of the input.
# In that case we declared the input as integer
# If we do not, python is concatinating the values as strings 

# x = int(input("What is x? "))
# y = int(input("What is y "))

# z = x + y
# print(z)
# improved version, we do not need the var z
# print(x+y)
# maybe we want to use the variable for further operations, 
# then it might be better to use the extra variable
# as long the code is readable, both versions seems to be valid code

# a = float(input("What is a? "))


# b = float(input("What is b? "))
# print(round(a+b,2))

def main():
  x = int(input("What is x? "))
  print("x squared is:", square(x))

def square(n):
  return n * n

main()