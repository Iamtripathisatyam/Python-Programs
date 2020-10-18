# a=input("What is Your Name : ")
# b=int(input("Your Earning of One Year : "))
# if b==0:
#     raise ZeroDivisionError("Zero is not Allowed !! because your salary can't be zero")
# if a.isnumeric():
#     raise Exception("Here Numbers are not Allowed...")
# print(f"Hello @{a} Your salary is enough !! Good")





# a=input("Please Enter your name : ")
# a=a.lower()
# try:
#     print(b)
# except Exception as e:
#     if a=="satyam" or a=="satyam empire" or a=="satyam tripathi":
#         raise ValueError(f"{a} is not Allowed !!")
#     print("Good !!")



#---------------------------Python Console --> Diff b/w is & == ---------------------------------------
# >>> a=[5,4,3,2,1]
# >>> b==a
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'b' is not defined
# >>> b=a
# >>> b==a
# True
# >>> b is a
# True
# >>> a
# [5, 4, 3, 2, 1]
# >>> b[0]=100
# >>> a
# [100, 4, 3, 2, 1]
# >>> b==a
# True
# >>> b is a
# True
# >>> c=a[:]
# >>> c
# [100, 4, 3, 2, 1]
# >>> c==a
# True
# >>> c is a
# False
# >>> c is b
# False
# >>>
