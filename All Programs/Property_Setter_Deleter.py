class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        # self.email=f"{lname}{fname}5352@gmail.com"
    def explain(self):
        return f"This is {self.fname} {self.lname}"
    # def printemail(self):
    #     pass
    @property  #if you don't want to call function  with () Braces in end then we use this func..
    def email(self):
        if self.fname == None or self.lname == None:
            return "Warning !! Not found !! Email has been deleted !!"
        return f"{self.fname}.{self.lname}@mahobagmail.com"
    @email.setter
    def email(self,string):
        # print("Setting...")
        names=string.split("@")[0]
        self.fname=names.split(".")[0]
        self.lname=names.split(".")[1]
    @email.deleter
    def email(self):
        self.fname=None
        self.lname=None


satyam=Employee("Satyam","Tripathi")
shivam=Employee("Shivam","Tripathi")
# print(satyam.explain())
# print(shivam.explain())
# print(satyam.email)
# print(satyam.email())
satyam.fname="Empire"
# print(satyam.email)
# print(satyam.email())
# print(satyam.email)
# satyam.email="satyam.psit@26390gmail.com"
# print(satyam.fname)
# print(satyam.lname)
# print(satyam.email)
# del satyam.email
# print(satyam.email)
# satyam.email="Satyam.empire26390@gmail.com"
# print(satyam.email)
# print(type(satyam))
# print(id(satyam))
# print(id("Hello !! Satyam"))
# o="Hi !! Empire"
# print(dir(o))
# print(dir(satyam))
# import inspect
# print(inspect.getmembers(satyam))
