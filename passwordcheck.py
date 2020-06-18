userPW=input("What is your password? ")
error = 0
if (len(userPW)<6)|(len(userPW)>16):
    print("Password invalid. Must be at least 6 characters long but no more than 16.")
    error+=1
lowerCount = 0
upperCount = 0
numCount = 0
symCount = 0
lowerCase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
upperCase = ["A", "B", "C", "D", "E", "F", 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', "Y", "Z"]
numCase = ['1','2','3','4','5','6','7','8','9', '0']
symCase=["@", "#", "!", "'"]

i=0
for i in range(len(userPW)):
    if userPW[i] in lowerCase:
        lowerCount+=1
    if userPW[i] in upperCase:
        upperCount+=1
    if userPW[i] in numCase:
        numCount+=1
    if userPW[i] in symCase:
        symCount+=1
if error>=1:
    print("")
else:
    if (lowerCount>=1):
        if (upperCount>=1):
            if (numCount>=1):
                if (symCount>=1):
                    print("Your password is fantastic!")
                else:
                    print("Your password needs at least one of these symbols: !, @, #")
            else:
                print("Your password needs at least one number")
        else:
            print("Your password needs at least one upper case letter")
    else:
        print("Your password needs at least one lower case letter")
