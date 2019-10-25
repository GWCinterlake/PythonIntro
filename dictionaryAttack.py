#open dictionary into var
dopen = open("dictAttack.txt", "r")
dictList = dopen.readlines()
dopen.close()
#store pw input as var
bday=input("What's your birth year? ")
year=input("What year is it? ")
pw = input("Let's test your password! Type it in: ")
#strip pw, lower case it
pwClean = pw.strip().lower()
#for loop
x=0
weak=0
length=len(dictList)
word=0
yrList=[]
yearfind=0
for bday in range(bday, year+1):
    yrList.append(bday)
    bday+=1
#finds if identifiable
for i in dictList:
    iClean=i.strip().lower()
    if iClean in pwClean:
        weak+=1
        word+=1
        iNew=iClean+yrList[i].strip()
        if iNew in pwClean:
            weak+=1
            yearfind+=1
    else:
        iNew=iClean+yrList[i].strip()
        if iNew in pwClean:
            weak+=1
            yearfind+=1
        else:
            x+=1
if yearfind>0:
    print("We found this year in your password")
if bdayfind>0:
    print("We found your birth year in your password")
if word>0:
    print("We found ",word," words in your password.")
if weak > 0:
    print("Weak password! :( ")
if x >= length:
    print('Fantastic password! :)')




    #if loop to compare to dictionary(stripped, lower)
