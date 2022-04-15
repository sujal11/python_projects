import random
# Rock,paper,scissor (GAME)
def game1(computer,you):
   if(computer==you):
       return None
   elif(computer=='R'):
       if you=='P':
           return True
       elif you=='S':
           return False
   elif(computer=='P'):
       if you=='S':  
           return True   
       elif you=='R':
           return False                             
   elif(computer=='S'):
       if you=='R':
           return True
       elif you=='P':
           return False

print("Computer chose: Rock(R) Paper(P) or Scissor(S)?")
randNo=random.randint(1,3)
if randNo==1:
    computer='R'
elif randNo==2:
    computer='P'   
elif randNo==3:
    computer='S' 

you=input("You chose: Rock(R) Paper(P) or Scissor(S)?")    
a=game1(computer,you)

print(f"Computer chose {computer}")
print(f"You chose {you}")

if a==None:
    print("The game is tie")
elif a==True:
    print("You win!")
else:
    print("You lose!")        
