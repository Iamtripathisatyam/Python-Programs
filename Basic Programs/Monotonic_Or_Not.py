######################################  1st Method ##############################

def monotonic(a):
    if (all([a[i]<=a[i+1] for i in range(len(a)-1)])) or (all([a[i]>=a[i+1] for i in range(len(a)-1)])):
        return True
    else:
        return False

a=[]
n=int(input("Enter the Number of Elements: "))
for i in range(0,n):
    element=int(input())
    a.append(element)

if monotonic(a):
    print("Yes, It's a Monotonic")
else:
    print("No, It's not a Monotonic")
    
    
    
    
    ######################################  2nd Method ##############################
    
def monotonic(a):
return (all([a[i]<=a[i+1] for i in range(len(a)-1)])) or (all([a[i]>=a[i+1] for i in range(len(a)-1)]))
a=[]
n=int(input("Enter the Number of Elements: "))
for i in range(0,n):
    element=int(input())
    a.append(element)

if monotonic(a):
    print("Yes, It's a Monotonic")
else:
    print("No, It's not a Monotonic")
