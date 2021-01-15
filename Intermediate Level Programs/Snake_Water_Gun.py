import random
import winsound
sat=["s","w",'g']
freq=640
duration=1000
comp=0
user=0
chances=5
chance=0
print("\n\n\t\t\t\t\t\t\t\tWelcome To The SANKE , Water, GUN GAME Developed by : @ Satyam Tripathi & Company")
print("\nRules : \n1. You have only 5 chances !!\n2. S for Snake , W for Water , G for Gun !!")
while chance<chances:
   print("\nPlease Enter Your Choice : ")
   a=input()
   a=a.lower()
   b=random.choice(sat)
   if a==b:
       print("ALERT !! Matche Tie !! Please Try Again !!")
       print(f"You guess : {a} & Computer guess : {b}")
       print(f"Computer Points : {comp} & Your Point : {user}\n")
   elif a=="w" and b=="s":
       comp=comp+1
       print(f" You Lose !! You guess : {a} & Computer guess : {b}\n Computer Won \"1\" Point $$")
       print(f"Computer Points : {comp} & Your Point : {user}\n")
   elif a== "s" and b == "w":
       user= user + 1
       print(f" You Won !! You guess : {a} & Computer guess : {b}\n YOU Won \"1\" Point $$")
       print(f"Your Point : {user} & Computer Points : {comp}\n")
   elif a== "s" and b == "g":
       comp = comp + 1
       print(f" You Lose !! You guess : {a} & Computer guess : {b}\n Computer Won \"1\" Point $$")
       print(f"Computer Points : {comp} & Your Point : {user}\n")
   elif a == "g" and b == "s":
       user= user + 1
       print(f" You Won !! You guess : {a} & Computer guess : {b}\n YOU Won \"1\" Point $$")
       print(f"Your Point : {user} & Computer Points : {comp} \n")
   elif a == "w" and b == "g":
       user= user + 1
       print(f" You Won !! You guess : {a} & Computer guess : {b}\n YOU Won \"1\" Point $$")
       print(f"Your Point : {user} & Computer Points : {comp}\n")
   elif a== "g" and b == "w":
       comp = comp + 1
       print(f" You Lose !! You guess : {a} & Computer guess : {b}\n Computer Won \"1\" Point $$")
       print(f"Computer Points : {comp} & Your Point : {user}\n")
   else:
       winsound.Beep(freq,duration)
       winsound.Beep(freq, duration)
       winsound.Beep(freq, duration)
       print("WARNING !! Wrong Input !!")

   chance=chance+1
   print(f"{chances-chance}  Chances left out of {chances}\n")

print("!! GAME OVER !!")
if comp==user:
    print("Match DRAW !!  because both have same points !!")
elif comp>user:
    print("You loose the GAME !! ")
else:
    print("GOOD !! You Won the GAME !!")

print(f"Your Points : {user} & Computer Points : {comp}\n\n")
