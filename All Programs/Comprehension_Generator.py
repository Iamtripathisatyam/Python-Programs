print("\n\n\n\t\t\tWelcome to the Comprehension Generator : Developed by : @Satyam Tripathi & Comapny\n\n")
while True:
 dict1 = {1: "\"List Comprehension\" !!", 2: "\"Dictionary Comprehension\" !!", 3: "\"Set Comprehension\" !!"}
 for key,value in dict1.items():
    print(f"Press : {key}. For {value}")
 user = int(input())
 if user == 1:
    num = int(input("How many ITEMS would you like to ADD in Your List : "))
    lst=[(input(f"Enter your {i+1} input : ")) for i in range(num)]
    print("$$ Your List $$ ")
    print(lst)
 elif user == 2:
    num = int(input("How many ITEMS would you like to ADD in Your DICTIONARY : "))
    dict = {input(f"Enter your {i+1} Key : "):input(f"Enter your {i+1} Value : ") for i in range(num)}
    print("$$ Your Dictionary $$")
    print(dict)
 elif user == 3:
    num = int(input("How many ITEMS would you like to ADD in Your SET : "))
    a={(input(f"Enter your {i+1} element : "))for i in range(num)}
    print("$$ Your Set $$")
    print(a)
 else:
    print("Warning !! Wrong Input")

 print("Do you Want to Continue : Prees[y/n]")
 choice=input()
 choice=choice.lower()
 if choice=="y":
    continue
 else:
     exit()
