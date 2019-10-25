Var = True
print("Written by Suhyun and Bianca")
while Var == True:
    answer1 = input("Should I go walk on the beach, go inside, or go to the city? ")
    if answer1 in " go walk on the beach ":
        answerbeach = input("Should I go swimming or make a sandcastle? ")
        if answerbeach in " make a sandcastle ":
            print("Wow, my sandcastle is very tall!")
        elif answerbeach in " go swimming ":
            print("Shark!")
        else:
            print("Please write swimming or sandcastle. ")
            answerbretry = input("Should I go swimming or make a sandcastle today? ")
            if answerbretry in " make a sandcastle ":
                print("Wow, my sandcastle is very tall!")
            elif answerbretry in " go swimming ":
                print("Shark!")
    elif answer1 in " go inside ":
        answerinside = input("Should I go sleep or make lunch? ")
        if answerinside in " go sleep ":
            print("I think I am going to take a nap.")
        elif answerinside in " make lunch ":
            print("I think I am going to cut carrots.")
            print("Aah! I cut myself!")
        else:
            print("Please write sleep or lunch. ")
            answeriretry = input("Should I go sleep or make lunch now? ")
            if answeriretry in " go sleep ":
                print("I think I am going to take a nap.")
            elif answeriretry in " make lunch ":
                print("I think I am going to cut carrots.")
                print("Aah! I cut myself!")
    elif answer1 in "go to the city":
        answercity = input("Should I go to court or go see a movie? ")
        if answercity in " go to court ":
            print("Let's make a jury!")
        elif answercity in " go see a movie ":
            print("This movie is boring :(")
        else:
            print("Please write court or movie.")
            answercretry = input("Should I go to court or go see a movie today? ")
            if answercretry in " go to court ":
                print("Let's make a jury!")
            elif answercretry in " go see a movie ":
                print("This movie is boring :(")
    else:
        print("Please write beach, inside, or city. Restart!" )
    Var = False
    restart = input("Restart? Yes/No ")
    if  restart == "yes":
        Var = True
    if restart == "no":
        Var = False
