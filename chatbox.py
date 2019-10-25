# --- Define your functions below! ---
RandomJokeBox = ["Broken pencil", "Hatch", "Kanga", "Ice cream", "Butter", "An extraterrestrial", "Beats", "Deja", "Doris"]
RandomPunchLine = ["Never mind, its POINTLESS", "Bless you!", "Actually, its 'KANGAROO'", "Ice cream if you dont let me in", "I butter tell you a few more jokes", "Wait, how many extraterrestrials do you know?", "Beats me", "Knock Knock", "Doris locked, thats why I'm knocking"]
HelloAnswers = ["hello", "hi", "hey", "hola", "buenos dias", "hello there", "hi to you", "hi there", "hi back"]
MoreJoke = ["yes!", "sure", "yeah", "of course", "why not", "sounds fun", "good", "lets do it", "id love to", "lets go"]
Yes=["yes!", "sure", "yeah", "of course", "why not", "sounds fun", "good", "lets do it", "id love to", "lets go"]
Help = ["help", "can you help me", "can i have some help"]
Stop = ["stop", "end", "go away" "bye", "you suck", "i hate this", "goodbye", "see you later", "see ya", "ciao", "ill see you later", "maybe next time", "never"]
PersonalExperience=["i", "we", "my mom", "my family", "my parents", "my sister", "my brother", "my siblings", "my aunt", "my grandmother"]
No=["no", 'nope', 'no thanks', 'nah', 'not now', 'not', 'sorry']

def isvalid(x,y):
    if x in y:
        return True
    else:
        return False
def intro():
    print("Hi there!")
    x=input("(What will you say?) ").lower()
    if isvalid(x,HelloAnswers) == True:
        print("I am a chatbot named Robert. I'm here to help with anything you need.")
        print("I can't wait to talk to you!")
    else:
        return
def askForMore():
    print("Wow, that's great! Can you tell me more about it? ")
    return
def hello():
    print("What's your name?")
    name = input("(What will you say?) ")
    print("Nice to meet you "+name+"! ")
def GhostJoke():
    print("Do you want to hear a ghost joke? ")
    answerGJ = input("(What will you say?) ").lower()
    print("That's the SPIRIT! Hahaha. Have you done anything fun this summer? ")
    return
def boring():
    print("Tell me more!")
    return
def stop():
    print("It was nice talking with you!")
    return
def joke(x):
    print("Knock knock! ")
    answer = input("(What will you say?) ").lower()
    if ("whos there" in answer) | ("who's there " in answer):
        print(RandomJokeBox[x])
        answer = input("(What will you say?) ").lower()
        if ("who" in answer):
            print(RandomPunchLine[x]+"! LOL! :) ")
        else:
            print("Say '"+RandomJokeBox[x]+" who' ")
            return
    else:
        print("Say 'who's there' ")
        answer = input("(What will you say?) ").lower()
        if ("whos there" in answer) | ("who's there " in answer):
            print(RandomJokeBox[x])
            answer = input("(What will you say?) ").lower()
            if ("who" in answer):
                print(RandomPunchLine[x]+"! LOL! :) ")
            else:
                print("Say '"+RandomJokeBox[x]+" who' ")
                return
def otherJoke():
    print("Should we do another one? ")
    s = input("(What will you say?) ").lower()
    if isvalid(s, MoreJoke):
        joke(t)
    else:
        return
# --- Put your main program below! ---
def main():
  intro()
  hello()
  GhostJoke()
  i=0
  t=0
  while True:
    answer = input("(What will you say?) ").lower()
    if i>=5:
        if t>=9:
            t=0
        print("Let's do a joke!")
        joke(t)
        t+=1
        otherJoke()
        i=0
        continue
    if isvalid(answer, Yes)|isvalid(answer,No):
        i+=1
        boring()
        continue
    if ("i" in answer)|("we" in answer)|("my" in answer):
        i+=1
        askForMore()
        continue
    if isvalid(answer, Stop):
        i+=1
        stop()
        return
    if isvalid(answer, Help):
        print("I can help!")
        a = input("What can I help you with? ").lower()
        print("Oh, I'm sorry, I don't know how to help with "+a+".")
    else:
        i+=1
        print("That's cool! Did you do anything recently?")


# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
    main()
