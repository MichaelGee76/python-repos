def main():
  x = int(input("What's X? "))
  if is_even(x):
    print("Number is even")
  else:
    print("Number is odd")

# pythonic way to write? me don't like
# def is_even(n):
#   return True if n % 2 == 0 else False

def is_even(n):
  if n % 2 == 0:
    return True
  else:
    return False      
  
main()  