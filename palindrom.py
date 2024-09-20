def main():
  #ask user for a sentence
  sentence = input("Check your sentence: ").lower().strip().replace(" ", "").replace(",", "").replace(".", "").replace(";", "").replace("!", "").replace("?", "")
  sentence_reversed = "".join(reversed(sentence))

  # check if sentence is a palindrome. 
  # output It's a palindrome/ It's not a palindrome
  if sentence == sentence_reversed:
    print("It's a palindrome.")
  else:
    print("Not a palindrom.")  



main()  