emoticon = "v.v"

def main():
    global emoticon
    say("Are you there?")
    emoticon = ":D"
    say("Cool, hi!")

def say(phrase):
  print(phrase + " " + emoticon)  

main()  