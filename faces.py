def convert():
  happy = "🙂"
  sad = "🙁"
  usr_string = input("Type something with a emoticon: ")
  if ":)" in usr_string and ":(" in usr_string:
    return usr_string.replace(":)", happy).replace(":(", sad)
  elif ":)" in usr_string:
    return usr_string.replace(":)", happy)
  elif ":(" in usr_string:
    return usr_string.replace(":(", sad)
  else:
    return usr_string
  
def main():
  
  print(convert()) 

main()   


