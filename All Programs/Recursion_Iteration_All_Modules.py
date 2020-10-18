## Recursion & Iteration !!
# def fact_iterative(n):
#     fac=1
#     for i in range(n):
#         fac = fac * (i+1)
#     return fac
# def fact_recursive(n):
#     if n==1:
#         return 1
#     else:
#         fac = n * fact_recursive(n-1)
#     return fac
# def fibbo(a):
#     if a==1:
#         return 0
#     elif a==2:
#         return 1
#     else:
#         return fibbo(a-1) + fibbo(a-2)

# a=int(input("कृपया एक अंक डालिये : "))
# print("फ़ैक्टोरियल ITERATION तरीके की मदद से : ",fact_iterative(a))
# print("फ़ैक्टोरियल RECURSION तरीके की मदद से : ",fact_recursive(a))
# a=int(input("कृपया एक अंक डालिये : "))
# print(fibbo(a))

# def first(a):
#     return a[1]
# a=[[5,1],[4,2],[8,2],[1,20]]
# a.sort(key=first)
# a.sort(key=lambda x:x[1])
# print(a)
# a=lambda x,y : x-y
# print(a(4,5))

## Modules
# import random
# a=random.randint(0,100)
# print(a)
# a=random.random() * 6
# print(a)
# a=["Satyam Tripathi","Shivam Tripathi","Deep Tripathi"]
# b= random.choice(a)
# print(b)
# import math
# a=int(input("Please Enter The No. : "))
# fac = math.factorial(a)
# print("Factorial : ",fac)

# import time
#
# print("This is printed immediately.")
# time.sleep(2.4)
# print("This is printed after 2.4 seconds.")

# import platform
# x = platform.system()
# print("You are using : ",x)
# x = dir(platform)
# print("Directory of Platform : ",x)

# import math
# a=int(input("Please Enter The No. : "))
# square = math.sqrt(a)
# print("Square Root : ",square)

# import datetime
# # time = datetime.datetime.now()
# # print(time)
#
# import platform
# print("Processor is : ", platform.processor())
# print("Architecture  is : ", platform.architecture())
# print("System is : ", platform.system())
# print("Compiler is : ", platform.python_compiler())
#
# import turtle
# t = turtle.Turtle()
# t.shape("turtle")
# t.color("orange","red")
# def square (s,m):
#     for i in range(4):
#         t. speed(0)
#         t.fd(s)
#         t.lt(m)
# for circle in range(200):
#     square(100,90)
#     square(0,47)
#

# import keyword
# satyam=keyword.kwlist
#  #displays all the keywords
# for i  in satyam:
#     print(i)




# import webbrowser
# print("\n\nPlease Enter Any Valid URL of site : ")
# a=input()
# webbrowser.open(a)



# import wikipedia
# search = input("\n\n\n\t\t\tWelcome To The SATYAM'S BROWSER Developed & Designed by :"
#                "\ @Satyam Tripathi & Company\n\n\n What "
#                "Do You Want to \"SEARCH\" : ")
# result = wikipedia.summary(search,sentences=4)
# print("\n\n\t",result)


# import winsound
# duration = 100  # milliseconds
# freq = 640  # Hz
# winsound.Beep(freq, duration)
# winsound.Beep(freq, duration)
# winsound.Beep(freq, duration)

import turtle
star = turtle.Turtle()
turtle.bgcolor("skyblue")
star.shape("turtle")
star.color("red")
star.speed(1)
for i in range(20):
    star.forward(200)
    star.write("@ SATYAM TRIPATHI")
    star.right(144)
    star.right(144)
    star.left(144)
    star.forward(200)
print(star)

# import builtins
# bui=builtins.bin(8)
# print(bui)


# import pyautogui
# screenshot = pyautogui.screenshot()
# screenshot.save(r'C:\Users\Dell\Desktop\Photos\pythonscreenshot.jpg')

