import random
# Snake,water,gun (GAME)
def game1(computer,you):
   if(computer==you):
       return None
   elif(computer=='w'):
       if you=='s':
           return True  
       elif you=='g':  
           return False   
   elif(computer=='g'):   
       if you=='w':
           return True
       elif you=='s':
           return False
   elif(computer=='s'):
       if you=='g':
           return True
       elif you=='w':
           return False

print("Computer chose: Water(w) Gun(g) or Snake(s)?")
randNo=random.randint(1,3)
if randNo==1:
    computer='w'
elif randNo==2:
    computer='g'   
elif randNo==3:
    computer='s' 

you=input("You chose: Water(w) Gun(g) or Snake(s)?")    
a=game1(computer,you)

print(f"Computer chose {computer}")
print(f"You chose {you}")

if a==None:
    print("The game is tie")
elif a==True:
    print("You win!")
else:
    print("You lose!")        




            
