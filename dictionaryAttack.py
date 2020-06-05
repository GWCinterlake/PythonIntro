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
print(pwClean)
#for loop
x=0
weak=0
length=len(dictList)
word=0
yrList=[]
yearfind=0
year1=int(year)
bday1=int(bday)
for bday1 in range(bday1, year1+1):
    yrList.append(bday1)
    bday1+=1
#finds if identifiable
for i in dictList:
    n=0
    iClean=dictList[n].strip().lower()
    if iClean in pwClean:
        weak+=1
        word+=1
        print(n)
        print(weak)
        print(word)
        iNew=iClean+yrList[n]
        if iNew in pwClean:
            weak+=1
            yearfind+=1
            print(weak)
            print(yearfind)
    else:
        iNew=iClean+str(yrList[n])
        print(iNew)
        if iNew in pwClean:
            weak+=1
            yearfind+=1
            print(weak)
            print(yearfind)
        else:
            x+=1
            print(x)

print(n)
print(x)
print(weak)
print(word)
print(yearfind)
if yearfind>0:
    print("We found this year in your password")
#if bdayfind>0:
    #print("We found your birth year in your password")
if word>0:
    print("We found ",word," words in your password.")
if weak > 0:
    print("Weak password! :( ")
if x >= length:
    print('Fantastic password! :)')




    #if loop to compare to dictionary(stripped, lower)
