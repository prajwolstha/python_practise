'''
1 for snake
-1 for water
0 for gun
'''
import random
print("Welcome to Snake Water Gun game")
computer = random.randint(-1,1)
youstr = input("Enter your choice : ")
youDict ={"s":1,"w":-1,"g":0}
reverseDict ={1:"Snake" ,-1:"Water",0:"Gun"}

if youstr not in youDict:
    print("Invalid input! Please enter 's' for Snake, 'w' for Water, or 'g' for Gun.")
    exit()
you = youDict[youstr]
print(f"You pick : {reverseDict[you]} \n Computer chose :{reverseDict[computer]}")
if(computer==you):
    print("Draw")
else:
        if(computer-you==-2 or computer-you==1):
         print("you win")
        else:
         print("you lose")
         

