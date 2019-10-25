print("Which numbers do you want to average?")
ages = [2, 2, 2]
sum = 0
i = 0
for i in range (len(ages)-1):
    sum = sum+ages[len(ages)-(i+1)]
    i+=1
print(sum/i)

def isEven(x):
    num=int(x)
    if num%2==0:
        print("True")
        return True
    else:
        print("False")
        return False
isEven(input("Check for even "))

def calcTotal(list):
    print(sum(list))
    return total
#string=input("What should I sum? ")
#i=0
#for i in range(len(string)-1):
#    print(int(string[i]))
#    num=int(string[i])
#    list.extend(num)
#    i+=1
list=[1,2,3,4,5,6]
print(list)
#calcTotal(list)
