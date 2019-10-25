cypher=input("What letter do you want you cypher rotation to start on? ").lower()
message=input("What is the message you want to code? ")
alphabet=['a', 'b', 'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alphaC=[]
mesS=[]
messageC=[]
x=0
y=0
difference=0
difP=0

#makes cyph
for a in range(0, 26):
    if alphabet[x]==cypher:
        x+=1
        place=y
        difference=25-abs(x-26)
        for b in range(y, 26):
            alphaC.append(alphabet[place])
            place+=1
        for c in range(0, difference):
            alphaC.append(alphabet[difP])
            #print(difP)
            #print(c)
            #print(alphaC)
            difP+=1
    else:
        x+=1
        y+=1

print("Cypher: "+"".join(alphaC))

#cyph message
for a in range(len(message)):
    print(a)
    mesS.append(message(a))
    print(mesS)
print(messageC)
