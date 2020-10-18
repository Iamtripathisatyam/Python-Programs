import time
def searcher():
    with open("codewithsatyam.txt") as tripathi:
      time.sleep(2)
      b=tripathi.read()
    while True:
        text=(yield )
        if text in b:
            print("Text is Found !!")
        else:
            print("Text is not Found")
search=searcher()
print("Searcher Starting...")
next(search)
while True:
 print("\nPlease Enter your name : ")
 a=input()
 a=a.lower()
 search.send(a)
 print("Do you Want to Continue : Prees[y/n]")
 choice = input()
 choice = choice.lower()
 if choice == "y":
     continue
 else:
     exit()
