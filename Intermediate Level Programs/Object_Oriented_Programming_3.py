# class Student:
#     no_of_leaves=10
#     def __init__(self,aname,astd,asec,ayear,apockmon):
#         self.name=aname
#         self.std=astd
#         self.sec=asec
#         self.year=ayear
#         self.pockmon=apockmon
#
#     # def details(self):
#     #     return f" Name : {self.name} \n Class : " \
#     #         f"{self.std} \n Section : {self.sec} \n Year :" \
#     #         f" {self.year} \n Pocket Money : {self.pockmon}\n"
#
#     # @classmethod
#     # def no_of_leaves(cls,satleaves):
#     #     cls.no_of_leaves=satleaves
#     @classmethod
#     def fromstr(cls,string):
#         # mullu=string.split("-")
#         # print(mullu)
#         # return cls(mullu[0],mullu[1],mullu[2],mullu[3],mullu[4])
#         return cls(*string.split("-"))
#
#
# # satyam = Student("Satyam Tripathi","B.tech in CS Branch","D","1st Year",10000)
# # shivam = Student("Satyam Tripathi","B.tech in CS Branch","D","1st Year",10000)
# kallu = Student.fromstr("Satyam Empire Tripathi-B.tech in CS branch-D-1st Year-10000")
# # shivam.no_of_leaves(2500)
# # print(satyam.no_of_leaves)
# print(kallu.name)
# print(kallu.std)
# print(kallu.sec)
# print(kallu.year)
# print(kallu.pockmon)



# class Student:
#     @staticmethod
#     def sattu(string):
#         print("This Is : " +string)
#
# deep=Student()
# deep.sattu("Satyam Empire")
