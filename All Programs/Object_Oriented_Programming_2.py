# class Student:
#       def details(self):
#           return f" Name : {self.name} \n Class : " \
#               f"{self.std} \n Section : {self.sec} \n Year :" \
#               f" {self.year} \n Pocket Money : {self.pockmon}\n"
#
#
# satyam=Student()
# shivam=Student()
# deep=Student()
# satyam.name="Satyam Empire Tripathi"
# satyam.std="B.tech In Computer Science & Engineering"
# satyam.sec="D"
# satyam.year="2nd Year"
# satyam.pockmon=10000
#
# shivam.name="Shivam Tripathi"
# shivam.std="10th Standard"
# shivam.sec="B"
# shivam.year="1st Year"
# shivam.pockmon=100
#
# deep.name="Deep Tripathi"
# deep.std="12th Standard"
# deep.sec="B"
# deep.year="1st Year"
# deep.pockmon=1000
#
# print(satyam.details())
# print(deep.details())
# print(shivam.details())


# class Student:
#     def __init__(self,aname,astd,asec,ayear,apockmon):
#         self.name=aname
#         self.std=astd
#         self.sec=asec
#         self.year=ayear
#         self.pockmon=apockmon
#
#     def details(self):
#         return f" Name : {self.name} \n Class : " \
#             f"{self.std} \n Section : {self.sec} \n Year :" \
#             f" {self.year} \n Pocket Money : {self.pockmon}\n"
#
#
# satyam = Student("Satyam Tripathi","B.tech in CS Branch","D","1st Year",10000)
# # shivam = Student()
# # deep = Student()
#
#
# # print(satyam.details())
# # print(deep.details())
# # print(shivam.details())



# class Student:
#     no_of_leaves=10
#     def __init__(self,aname,astd,asec,ayear,apockmon):
#         self.name=aname
#         self.std=astd
#         self.sec=asec
#         self.year=ayear
#         self.pockmon=apockmon
#
#     def details(self):
#         return f" Name : {self.name} \n Class : " \
#             f"{self.std} \n Section : {self.sec} \n Year :" \
#             f" {self.year} \n Pocket Money : {self.pockmon}\n"
#
#     @classmethod
#     def no_of_leaves(cls,satleaves):
#         cls.no_of_leaves=satleaves
#
# satyam = Student("Satyam Tripathi","B.tech in CS Branch","D","1st Year",10000)
# shivam=Student("Satyam Tripathi","B.tech in CS Branch","D","1st Year",10000)
# shivam.no_of_leaves(2500)
# print(satyam.no_of_leaves)
