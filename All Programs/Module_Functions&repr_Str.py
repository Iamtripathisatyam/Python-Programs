class player:
    def __init__(self,aname,agame,atrophy,amedal,ayear):
        self.name=aname
        self.game=agame
        self.trophy=atrophy
        self.medal=amedal
        self.year=ayear

    def printdetails(self):
        return f" Name of Player: {self.name} \n Game  : " \
            f"{self.game} \n Trophies : {self.trophy} \n Medals :" \
            f" {self.medal} \n Year : {self.year} \n "

    # def __add__(self, other):
    #     return self.year+other.year
    # def __truediv__(self, other):
    #     return self.year/other.year
    # def __mul__(self, other):
    #     return self.year*other.year
    # def __mod__(self, other):
    #     return self.year%other.year
    # def __repr__(self):
    #     return f"I am : {self.name} I love : {self.game} Trophy gain by me : {self.trophy} medals gain by me :  {self.medal} in the Year : {self.year}"
    # def __pow__(self, power, modulo=None):
    #     return self.year**power.year
    # def __repr__(self):
    #     return self.printdetails()
    # def __repr__(self):
    #     return f" Name of Player: {self.name} \n Game  : " \
    #         f"{self.game} \n Trophies : {self.trophy} \n Medals :" \
    #         f" {self.medal} \n Year : {self.year} \n "

    def __repr__(self):
          return f"Player : '{self.name}','{self.game}','{self.medal}','{self.trophy}',{self.year}"
    def __str__(self): # Program will give the first priority to the STR Function ....
        return f" Name of Player: {self.name} \n Game  : " \
            f"{self.game} \n Trophies : {self.trophy} \n Medals :" \
            f" {self.medal} \n Year : {self.year} \n "
a1=satyam=player("Satyam Tripathi",["Cricket","Vollyball","Football"],
                    "Bharat Ratna",["Silver"
                           ,"Bronze","Gold"],5)
a2=player("Shivam Tripathi",["Cricket","Vollyball","Football"],
                    "Bharat Ratna",["Silver"
                           ,"Bronze","Gold"],2)
# print(a1+a2)
# print(a1/a2)
# print(a1*a2)
# print(a1%a2)
# print(a1)
# print(a2)
# print(pow(a1,a2))
print(a2)
print(repr(a1))
print(str(a1))
