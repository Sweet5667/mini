#HANGMAN GAME USING PYTHON

name=input("enter your name: ")
print("welcome",name,"all the best")
turn=10
mind="laptop"
letters=""
while turn>0:
    lose=0
    count=0
    for i in mind:
        if i in letters:
            print(i,end=" ")
        else:
            print("_",end=" ")
            count+=1
    print()    
    if count==0:
        print("\nyou won")
        break
    guess=(input("\nguess any character: "))    
    letters+=guess    
    
    if guess not in mind:
        turn-=1
        print("\nwrong guess \nyou have",turn,"chances left")
    