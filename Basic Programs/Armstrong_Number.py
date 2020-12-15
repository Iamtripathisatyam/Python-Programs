def order(a):
    c=0
    while a>0:
        a//=10
        c+=1
    return c
def Arm(a):
    temp=a
    c=order(a)
    sum=0
    while temp>0:
        dig=temp%10
        sum=sum+dig ** c
        temp//=10
    return "It's an Armstrong Number" if(sum==a) else "No, it's not an Armstrong Number"


a=int(input("Enter a Number: "))
print(f"{Arm(a)}")
