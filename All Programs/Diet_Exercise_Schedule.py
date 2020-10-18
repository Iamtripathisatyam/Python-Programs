# HEALTH MANAGEMENT SYSTEM !!!
import datetime
def gettime():
    return datetime.datetime.now()

def take(tri):
    if tri == 1:
        sit = int(input("\n1. For EXERCISE !!\n2. For DIET !!\n Please Enter Your Choice : "))
        if (sit == 1):
            value=input("Now You can write here : ")
            with open("satyam-food.txt", "a") as f:
                f.write("Date & Time : "+ str(gettime()) + " : " + value + "\n")
            print("!! SUCCESSFULLY WRITEEN !!")
        elif (sit == 2):
            value = input("Now You can write here : ")
            with open("satyam-ex.txt", "a") as f:
                f.write("Date & Time : "+ str(gettime())+ " : " + value + "\n")
            print("!! SUCCESSFULLY WRITEEN !!")
    elif (tri == 2):
            sit = int(input("\n1. For EXERCISE !!\n2. For DIET !!\n Please Enter Your Choice : "))
            if (sit == 1):
                value = input("Now You can write here : ")
                with open("shivam-food.txt", "a") as f:
                    f.write("Date & Time : " + str(gettime()) + " : " + value + "\n")
                print("!! SUCCESSFULLY WRITEEN !!")
            elif (sit == 2):
                value = input("Now You can write here : ")
                with open("shivam-ex.txt", "a") as f:
                    f.write("Date & Time : " + str(gettime()) + " : " + value + "\n")
                print("!! SUCCESSFULLY WRITEEN !!")
    elif (tri== 3):
            sit = int(input("\n1. For EXERCISE !!\n2. For DIET !!\n Please Enter Your Choice : "))
            if (sit == 1):
                value = input()
                with open("deep-food.txt", "a") as f:
                    f.write("Date & Time : " + str(gettime()) + " : " + value + "\n")
                print("!! SUCCESSFULLY WRITEEN !!")
            elif (sit == 2):
                value = input()
                with open("deep-ex.txt", "a") as f:
                    f.write("Date & Time : " + str(gettime()) + " : " + value + "\n")
                print("!! SUCCESSFULLY WRITEEN !!")
    else:
        print("WARNING !! Please Enter the VALID input !!")


def retrieve(tri):
    if tri == 1:
        sit = input("\n1. For EXERCISE !!\n2. For DIET !!\n Please Enter Your Choice : ")
        if (sit == "1"):
            with open("satyam-food.txt") as f:
                print("Details of SATYAM TRIPATHI : \n")
                for data in f:
                    print(data, end="")
        elif (sit == "2"):
            with open("satyam-ex.txt") as f:
                print("Details of SATYAM TRIPATHI : \n")
                for data in f:
                    print(data, end="")
    elif (tri == 2):
        sit = int(input("\n\n1. For EXERCISE !!\n2. For DIET !!\n Please Enter Your Choice : "))
        if (sit == 1):
            with open("shivam-food.txt") as f:
                print("Details of SHIVAM TRIPATHI : \n")
                for data in f:
                    print(data, end="")
        elif (sit == 2):
            with open("shivam-ex.txt") as f:
                print("Details of SHIVAM TRIPATHI : \n")
                for data in f:
                    print(data, end="")
    elif (tri == 3):
        sit = int(input("\n1. For EXERCISE !!\n2. For DIET !!\n Please Enter Your Choice : "))
        if (sit == 1):
            with open("deep-food.txt") as f:
                print("Details of DEEP TRIPATHI : \n")
                for data in f:
                    print(data, end="")
        elif (sit == 2):
            with open("deep-ex.txt") as f:
                print("Details of DEEP TRIPATHI : \n")
                for data in f:
                    print(data, end="")
    else:
        print("WARNING !! Please Enter the VALID input !!")


print("\n\n\t\tWelcome To The HEALTH MANAGEMENT SYSTEM Developed by : @ SATYAM TRIPATHI & COMPANY")
mah=input("\n1. For LOG !!\n2. For RETRIEVE !!\nPlease Enter your choice : ")
if mah=="1":
    tri=int(input("\nWhose Details You want to LOG : \n\n1. SATYAM TRIPATHI\n2. SHIVAM TRIPATHI\n3. DEEP TRIPATHI\n Please Enter Your Choice : "))
    take(tri) # Here We call the function : take !!
else:
    tri = int(input("Whose Details You want to RETRIEVE : \n1. SATYAM TRIPATHI\n2. SHIVAM TRIPATHI\n3. DEEP TRIPATHI\n Please Enter Your Choice : "))
    retrieve(tri) # Here We call the function : retrieve !!

