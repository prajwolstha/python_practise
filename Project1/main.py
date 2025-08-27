'''
1 for snake
-1 for water
0 for gun
'''

computer = -1
youstr = input("Enter your choice : ")
youDict ={"s":1,"w":-1,"g":0}
you = youDict[youstr]
if(computer==-1 and you ==1):
    print("you win")

elif(computer == 1 and you ==0):
    print("you lose")





    
