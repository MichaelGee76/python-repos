my_guess = 5

def main():
  user_guess = int(input("guess a number between 0-9 "))
  print(type(user_guess))
  if user_guess == my_guess:
    print("thats correct")
  else:
    print("sorry, thats wrong")

main()    