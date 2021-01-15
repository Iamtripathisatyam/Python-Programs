#----------------------------------------------Else with for loop--------------------------------------------

# import time
# dryfruits=["Almonds","Betel Nut","Cashew","Dates Dried","Cudpahnut","Raisin","Dates","Walnuts","Seasame Seeds","Prunes","Lotus Seeds Pop"]
# for dry in dryfruits:
#     print(dry)
#     time.sleep(0.5)
# else:
#     print("Here For loop ended !!")

# for dry in dryfruits:
#     if dry=="dal":
#      break
# else:
#     print("Here For loop ended !!")

#---------------------------Else & Finally in Try except------------------------------------------------



# f1=open("satyam.txt")
# try:
#     f=open("oye.txt")
# except Exception as e:
#     print(e)
# else:
#     print("This will Run Only if Except is not running")
# finally:
#     print("Running Anyway !!")
#     f1.close()
#
# print("Here comes the money !! Money John Cena ")




# f1=open("satyam.txt")
# try:
#     f=open("oyes.txt")
# except Exception as e:
#     print(e)
# else:
#     print("Now here it will not run because except method will be run there !!")
# finally:
#     print("Running Anyway !!")
#     f1.close()
#
# print("Here comes the money !! Money John Cena ")



# f1=open("satyam.txt")
# try:
#     f=open("oyes.txt")
# except EOFError as e:
#     print("Here End of file error has come !!")
# except IOError as e:
#     print("IO Error has come !! Please be aware !!")
# else:
#     print("Now here it will not run because except method will be run there !!")
# finally:
#     print("Running Anyway !!")
#     f1.close()
# print("Here comes the money !! Money John Cena ")

#-------------------------------------Coroutines--------------------------------------------------------

# import time
# def searcher():
#     book="Satyam Tripathi belong to mahoba uttar pradesh !!"
#     time.sleep(3)
#     while True:
#         text=(yield )
#         if text in book:
#             print("Text is Found !!")
#         else:
#             print("Text is not Found")
#
# search=searcher()
# print("Searcher Started !!")
# print("It's time for next !!")
# next(search)
# # print(" next Started !!")
# search.send("Satyam")
# input("Press any key")
# search.send("Tripathi") ## from here it will not take 3 second it will start from while loop
# input("Press any key")
# search.send("belong")
# input("Press any key")
# search.send("to")
# input("Press any key")
# search.send("Mahoba")
# input("Press any key")
# search.send("uttar")
# input("Press any key")
# search.send("pradesh")
# input("Press any key")
# search.send("mahoba")
# input("Press any key")
# search.close()
# search.send("mahoba") ## here it will give error because we have alredy closed the SEARCH !!
# input("Press any key")

# import time
# def searcher():
#     with open("satyam.txt") as tripathi:
#       time.sleep(2)
#       b=tripathi.read()
#     while True:
#         text=(yield )
#         if text in b:
#             print("Text is Found !!")
#         else:
#             print("Text is not Found")
# search=searcher()
# print("Searcher Starting...")
# next(search)
# print("\nPlease Enter your name : ")
# a=input()
# search.send(a)
# input("Press Any Key :  ")
# print("\nPlease Enter your name : ")
# a=input()
# search.send(a)


# import time
# def name():
#     time.sleep(2)
#     with open("satyam.txt")as r:
#         # for data in r:
#         #     sa=data
#          var1 = r.read()
#
#     while True:
#         text = (yield)
#         if text in var1:
#             print("your text in founded ")
#         else:
#             print("your text in does not found")
# searc = name()
# next(searc)
# var1  = input("enter your text: ")
# searc.send(var1)
