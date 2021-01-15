yearAge = int(input("Please Enter your Age/Year of birth : "))
isAge = 0
isYear = 0
if len(str(yearAge)) == 4:
    isYear = 1
else:
    isAge = 1
if(yearAge<1900 and isYear==1):
    print("You Are the oldest person ALIVE !!")
    exit()
if(yearAge>2020):
    print(" Please Don't joking !! You are not yet born")
    exit()
if isAge==1:
    yearAge = 2020 - yearAge
print(f"You will be 100 years old in {yearAge + 100}")
interestedYear = int(input("\nEnter the year you want to know your age in\n"))
print(f"You will be {interestedYear - yearAge} years old in {interestedYear}")

