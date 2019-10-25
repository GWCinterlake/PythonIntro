fOpen=open('jeapordytestFile.txt', 'r')
fileString=fOpen
fOpen.close()
l1=[]
l2=[]
l3=[]
l4=[]
l5=[]
leng=len(fileString).strip()
if len(fileString)%5==0:
    for i in range(len(fileString)/5):
        x=0
        l1.append(fileString[x])
        l2.append(fileString[x+1])
        l3.append(fileString[x+2])
        l4.append(fileString[x+3])
        l5.append(fileString[x+4])
        x+=5
else:
    rem=len(fileString)%5
    for i in range(len(fileString)/5):
        x=0
        l1.append(fileString[x])
        l2.append(fileString[x+1])
        l3.append(fileString[x+2])
        l4.append(fileString[x+3])
        l5.append(fileString[x+4])
        x+=5
    if rem>3:
            l1.append(fileString[leng-4])
            l2.append(fileString[leng-3])
            l3.append(fileString[leng-2])
            l4.append(fileString[leng-1])
    if rem>2:
            l1.append(fileString[leng-3])
            l2.append(fileString[leng-2])
            l3.append(fileString[leng-1])
    if rem>1:
            l1.append(fileString[leng-2])
            l2.append(fileString[leng-1])
    if rem>0:
            l1.append(fileString[leng-1])
