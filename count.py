def main():
  # ask usr for a sentence
  sentence = input("Write a sentence: ")
  # count words in sentence 
  sentence_splitted = sentence.split()
  # print(type(sentence_splitted))
  # output how many words used in sentence
  print(f"You used {len(sentence_splitted)} words in your sentence and {len(sentence.replace(" ", ""))} characters.")



main()  