word=input("Player 1, enter a word! ")
print("Player 2, you have 7 lives. Good luck! ")
show=[]
answer=[]
i=0
for i in range (len(word)):
    show.extend("_")
    i+=1
print(show)
life=7
print(life)
while life>0:
    a=input("What's your guess? ")
    t=0
    f=0
    if a in word:
        for t in range (len(word)):
            if word[t]==a:
                if "_" in show:
                    if show[t]!=a:
                        show[t]=a
                        print(show)
                        if "_" not in show:
                            life=0
                            #print("Congrats, you win!")
                        else:
                            continue
                    else:
                        continue
                else:
                    continue
            else:
                f+=1
                t+=1
            #if f==len(word):
            #    life-=1
            #    f=0
            #    print(life)
            #else:
            #    continue
    else:
        life-=1
        print(life)
print("Game Over!")
print("Congrats, you win!")
