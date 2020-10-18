class Student:
    var=8
    def __init__(self,aname,astd,asec,ayear,apockmon,languages):
        self.name=aname
        self.std=astd
        self.sec=asec
        self.year=ayear
        self.pockmon=apockmon
        self.lan = languages

    def details(self):
        return f" Name : {self.name} \n Class : " \
            f"{self.std} \n Section : {self.sec} \n Year :" \
            f" {self.year} \n Pocket Money : {self.pockmon}\n"
class player:
    games=10
    var=9
    def __init__(self,aname,agame,atrophy,amedal):
        self.name=aname
        self.game=agame
        self.trophy=atrophy
        self.medal=amedal

    def printdetails(self):
        return f" Name of Player: {self.name} \n Game  : " \
            f"{self.game} \n Trophies : {self.trophy} \n Medals :" \
            f" {self.medal} \n"

class coolprogrammer(player,Student):
    var=10
    language=["C(programming language)","Python One level up"]
    def lang(self):
        print(self.language)

satyam=coolprogrammer("Satyam Tripathi",["Cricket","Vollyball","Football"],
                    "Bharat Ratna",["Silver"
                           ,"Bronze","Gold"])
# sattu = coolprogrammer("Satyam Tripathi","B.tech in CS Branch",
#                    "D","1st Year",10000,["C(programming Lnaguage)"
#                         ,"Python","Microsoft Word"])
#
# dat=satyam.printdetails()
# print(dat)
# satyam.lang()
# det=sattu.details()
# print(det)
print(satyam.var)
