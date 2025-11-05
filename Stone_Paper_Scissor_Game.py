"""
s = stone 
p = paper
r = scissor

"""

import random
a = 0
l = 0
t = 0
n = int(input("Enter the number of Rounds : "))
for i in range(1,n+1):
    computer = random.choice(['s', 'p', 'r'])

    youstr = input("\nEnter 's' or 'p' or 'r' = ")
    youdict = {"s":'s',"p":'p',"r":'r'}
    you = youdict[youstr]

    computerdict= {'s':"Stone",'p':"Paper",'r':"scissor"}
  
    print("you choose = ", computerdict[you])
    print("computer choose = ", computerdict[computer])

    if(computer==you):
        print("Its draw")
        t=t+1  
    else:
        if(computer=='s' and you =='p'):
            print("you win")
            a=a+1
        elif(computer=='s' and you =='r'):
            print("computer win")
            l=l+1
        elif(computer=='p' and you =='s'):
            print("computer win")
            l=l+1
        elif(computer=='p' and you =='r'):
            print("you win")
            a=a+1
        elif(computer=='r' and you =='s'):
            print("you win")
            a=a+1
        elif(computer=='r' and you =='p'):
            print("computer win")
            l=l+1
        else:
            print("Somthong wrong")
            
print("\nFinal Score:")
print("Wins:", a, "| Losses:", l, "| Draws:", t)

if a > l:
    print("\nCongratulations...")
    print("You are the Winner of this Game!")
elif l > a:
    print("\nWell played...\nBut")
    print("Computer is the Winner of this Game...")
else:
    print("\nIt's a Tie!")