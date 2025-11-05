import random 
a=0
l=0
t=0
round=int(input("Enter number round="))
for n in range(1,round+1):
    computer = random. choice ([ 1, -1, 0 ])
    youstr = input ("Enter your Choice : " )
    youDict = {"s" : 1, "w" : -1, "g" : 0}
    reverseDict = {1 : "Snake", -1 : "Water", 0 : "Gun"}

    you = youDict[youstr]

    print ("You Choose "+reverseDict[you])
    print ("Computer Choose "+reverseDict[computer])

    if(computer == you):
        print("It's Draw..")
        print (" ")
        t=t+1    
    else:
        if(computer == -1 and you == 1):
            print("You Win..") 
            print (" ")
            a=a+1
        elif(computer == -1 and you == 0):
            print("You Lose..") 
            print (" ")
            l=l+1
        elif(computer == 1 and you == -1):
            print("You Lose..") 
            print(" ")
            l=l+1
        elif(computer == 1 and you == 0):
            print("You Win..") 
            print (" ")
            a=a+1
        elif(computer == 0 and you == -1):
            print("You Win..")  
            print(" ")
            a=a+1
        elif(computer == 0 and you == 1):
            print("You Lose..")    
            print (" ")
            l=l+1   
        else:
            print ("Somthing Went Wrong..")
print("Final Score:")
print("Wins:", a, "| Losses:", l, "| Draws:", t)

if a > l:
    print("Congratulations...")
    print("You are the Winner of this Game!")
elif l > a:
    print("Well played...\nBut")
    print("Computer is the Winner of this Game...")
else:
    print("It's a Tie!")