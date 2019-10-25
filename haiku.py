import random
#answer1 = input("Can I have a number from 0-3 please? ")
#answer2 = input("Can I have another number? ")
#answer3 = input("One last number please! ")
list1=["The sun shines bright today", "Joy in life is rare", "Happiness is temporary", "As long as we're together"] #["I don't feel that well", "I am deeply in love", "Who is there to help", "No one understands me"]
list2=["The birds are chirping away", "Enjoy it while it remains", "We can make it last forever", "I hope to see you very soon"] #["This heartbreak is way to much", "I wish I could get over him", "Hearts will be healed with time, right?", "How can I fix what I've done"]
list3=["The world is thriving", "Lets go surfing now", "Tonight will fix all", "Lets code some more now!"] #["When will this pain stop", "Can I possibly be ok?", "Why is love so hard", "Peace will come in time"]
num1 = random.randint(0, len(list1) - 1)
num2 = random.randint(0, len(list2)-1)
num3 = random.randint(0, len(list3)-1)
print(list1[int(num1)])
print(list2[int(num2)])
print(list3[int(num3)])
