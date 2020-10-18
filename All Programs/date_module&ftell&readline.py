# f=open("mahoba.txt")
# print(f.tell())
# print(f.readline())
# print(f.tell())
# print(f.readline())
# print(f.tell())


# f=open("mahoba.txt")
# print(f.readline())
# f.seek(16)
# print(f.readline())
# f.close()


# with open("mahoba.txt") as f:
     # a=f.readlines()
    # a=f.read(15)
    # print(a)
# f=open("mahoba.txt")
# f.readline()  if we try to open this fiole again then it will through an error !!
# f.close()
# from datetime import date
#
# today = date.today()
# print("Today's date:", today)
import datetime
def gettime():
    return datetime.datetime.now()
print("date : "+gettime())



